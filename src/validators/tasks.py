from celery import shared_task

from src.validators.utils import contract_processor
from src.validators.models import Validator


@shared_task(name="update_active_validators_amounts")
def update_active_validators_amounts():
    validators, amount = contract_processor.get_active_validators_info()
    data = zip(validators, amount)
    for address, amount in data:
        validator = Validator.objects.filter(address=address).first()
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
        validator = Validator.objects.filter(address=address).first()
        if validator:
            validator.status = Validator.ValidatorStatus.STOPPED
            validator.save()


@shared_task(name="update_archived_validators")
def update_archived_validators():
    validators = contract_processor.get_stopped_validators_info()
    if validators is None:
        return None
    db_validators = Validator.objects.filter(status=Validator.ValidatorStatus.STOPPED).values_list('address', flat=True)
    validators_db_set = set(db_validators)
    difference = validators_db_set.difference(validators)
    for address in difference:
        validator = Validator.objects.filter(address=address).first()
        if validator:
            is_validator = contract_processor.is_validator(address)
            validator.status = Validator.ValidatorStatus.HEALTHY if is_validator else Validator.ValidatorStatus.ARCHIVED
            validator.save()
