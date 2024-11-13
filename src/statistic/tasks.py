from celery import shared_task

from src.validators.utils import contract_processor, ContractProcessorError
from src.statistic.models import DelegatorsInfo


@shared_task(name="update_total_delegators")
def update_total_delegators():
    try:
        validators, _ = contract_processor.get_active_validators_info()
        delegators = set()
        for validator in validators:
            delegators.update(contract_processor.get_delegator_info_per_validator(validator))
    except ContractProcessorError:
        return
    delegators_info, _ = DelegatorsInfo.objects.get_or_create()
    delegators_info.total_delegators = len(delegators)
    delegators_info.save()
