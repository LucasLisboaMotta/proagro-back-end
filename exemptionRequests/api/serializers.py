from rest_framework import serializers
from exemptionRequests import models

class ExemptionRequestsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.ExemptionRequests
    fields = '__all__'
