from celery import shared_task

from src.validators.utils import contract_processor
from src.statistic.models import DelegatorsInfo


@shared_task(name="update_total_delegators")
def update_total_delegators():
    validators, _ = contract_processor.get_active_validators_info()
    delegators = set()
    for validator in validators:
        delegators.add(contract_processor.get_delegator_info_per_validator(validator))
    delegators_info, _ = DelegatorsInfo.objects.get_or_create()
    delegators_info.total_delegators = len(delegators)
    delegators_info.save()
