from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Things(models.Model):
    name = models.CharField(
        max_length = 30,
        unique = True,
        blank = False,
    )
    description = models.CharField(
        max_length = 120,
        unique = False,
        blank = False,
    )
    quantity = models.IntegerField(
        unique = True,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
