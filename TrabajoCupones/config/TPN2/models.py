from django.db import models

# Create your models here.


class Descuentos(models.Model):
    name = models.CharField(max_length=255, default='')
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    DISCOUNT_CHOICES = [
        ('4', '4%'),
        ('12', '12%'),
        ('16', '16%'),
        ('28', '28%'),
    ]
    discount = models.CharField(max_length=3, choices=DISCOUNT_CHOICES)
    available = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.name}'