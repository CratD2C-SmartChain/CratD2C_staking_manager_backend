from django.db import models


class DelegatorsInfo(models.Model):
    total_delegators = models.DecimalField(
        max_digits=128,
        decimal_places=0,
        default=0,
        verbose_name='Total Delegators for all active validators',
    )
