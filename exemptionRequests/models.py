from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# Create your models here.

class ExemptionRequests(models.Model):
  
  class EventList(models.TextChoices):
    EXCESSIVE_RAIN = 'CHUVA EXCESSIVA', _('CHUVA EXCESSIVA')
    FROST = 'GEADA', _('GEADA')
    HAIL = 'GRANIZO', _('GRANIZO')
    DRY = 'SECA', _('SECA')
    GALE = 'VENDAVAL', _('VENDAVAL')
    LIGHTNING = 'RAIO', _('RAIO')
  
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  date = models.DateField()
  cpf = models.IntegerField()
  latitude_location = models.FloatField()
  longitude_location = models.FloatField()
  event = models.CharField(max_length=15, choices=EventList.choices)
  create_at = models.DateField(auto_now_add=True)
