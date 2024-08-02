from celery import shared_task

from src.validators.utils import contract_processor
from src.validators.models import Validator


@shared_task(name="update_active_validators_amounts")
def update_active_validators_amounts():
    data = contract_processor.get_active_validators_info()
    for address, amount in data:
        validator = Validator.objects.filter(address=address).first()
        if validator and validator.stake_amount != amount:
            validator.stake_amount = amount
            validator.save()
