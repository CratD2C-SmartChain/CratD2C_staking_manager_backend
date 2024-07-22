from django.db import models


class Validator(models.Model):
    
    class ValidatorStatus(models.TextChoices):
        CREATED = 'CREATED'
        HEALTHY = 'HEALTHY'
        STOPPED = 'STOPPED'
        ARCHIVED = 'ARCHIVED'

    status = models.CharField(
        choices=ValidatorStatus.choices,
        default=ValidatorStatus.CREATED,
        max_length=16,
        db_index=True,
    )
    name = models.CharField(max_length=120, verbose_name="Name")
    logo = models.ImageField(upload_to="validator_logo", verbose_name="Logo")
    stake_amount = models.DecimalField(
        verbose_name="Stake Amount",
        decimal_places=0,
        max_digits=128,
        default=0,
    )
    commission = models.DecimalField(
        verbose_name="Commission",
        decimal_places=0,
        max_digits=8,
        default=0,
    )
    start_block = models.DecimalField(
        verbose_name="Start Block",
        decimal_places=0,
        max_digits=128,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.CharField(
        max_length=128,
        verbose_name="Address",
        unique=True,
    )
