from rest_framework import viewsets
from exemptionRequests.api import serializers
from exemptionRequests import models

class ExemptionRequestsViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.ExemptionRequestsSerializer
  queryset = models.ExemptionRequests.objects.all()
