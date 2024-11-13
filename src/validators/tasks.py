from celery import shared_task
from django.db import transaction

from src.validators.utils import contract_processor, ContractProcessorError
from src.validators.models import Validator


@shared_task(name="update_active_validators_amounts")
def update_active_validators_amounts():
    try:
        validators, amounts = contract_processor.get_active_validators_info()
    except ContractProcessorError:
        return
    
    with transaction.atomic():
        for address, amount in zip(validators, amounts):
            validator = Validator.objects.select_for_update().filter(address__iexact=address).first()
            if validator:
                validator.stake_amount = amount
                if validator.status != Validator.ValidatorStatus.HEALTHY:
                    validator.status = Validator.ValidatorStatus.HEALTHY
                validator.save()

        db_validators = Validator.objects.filter(
            status=Validator.ValidatorStatus.HEALTHY).values_list('address', flat=True)
        validators_contract_set = set(validators)
        validators_db_set = set(db_validators)
        difference = validators_db_set.difference(validators_contract_set)

        for address in difference:
            validator = Validator.objects.select_for_update().filter(address__iexact=address).first()
            if validator:
                validator.status = Validator.ValidatorStatus.STOPPED
                validator.save()


@shared_task(name="update_archived_validators")
def update_archived_validators():
    try:
        validators, amounts = contract_processor.get_stopped_validators_info()
        with transaction.atomic():
            for address, amount in zip(validators, amounts):
                db_validator = Validator.objects.select_for_update().filter(address__iexact=validator).first()
                if db_validator:
                    db_validator.stake_amount = amount
                    db_validator.save()

            db_validators = Validator.objects.filter(status=Validator.ValidatorStatus.STOPPED).values_list('address', flat=True)
            validators_contract_set = set(validators)
            validators_db_set = set(db_validators)
            difference = validators_db_set.difference(validators_contract_set)

            for address in difference:
                validator = Validator.objects.select_for_update().filter(address__iexact=address).first()
                if validator:
                    is_validator = contract_processor.is_validator_active(address)
                    validator.status = Validator.ValidatorStatus.HEALTHY if is_validator else Validator.ValidatorStatus.ARCHIVED
                    validator.save()
    except ContractProcessorError:
        return
