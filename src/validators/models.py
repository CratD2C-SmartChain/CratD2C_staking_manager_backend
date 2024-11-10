from django.core.validators import FileExtensionValidator
from django.db import models

from src.utilities import network, config
from src.validators.validators import validate_image_size


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
    logo = models.ImageField(
        upload_to="validator_logo",
        verbose_name="Logo",
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_image_size
        ]
    )

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
    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True,
    )
    website = models.URLField(null=True, blank=True, verbose_name="Website")
    twitter = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    penalty = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=256,
        verbose_name="Penalty",
    )

    class Meta:
        ordering = ('-stake_amount', )

    @property
    def checkpoints(self):
        if not self.start_block:
            return 0
        return (network.block_number - self.start_block) // config.BLOCKCHAIN.EPOCH_LEN

    @property
    def performance_index(self):
        if self.checkpoints == 0:
            return 100
        return (
                (self.checkpoints - self.penalty) * 100 // self.checkpoints
        )

    @classmethod
    def validator_view_statuses(cls):
        return [cls.ValidatorStatus.HEALTHY, cls.ValidatorStatus.STOPPED]
