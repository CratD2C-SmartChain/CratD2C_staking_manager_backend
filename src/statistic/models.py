from django.db import models


class DelegatorsInfo(models.Model):
    total_delegators = models.DecimalField(max_digits=128, decimal_places=0, default=0)
