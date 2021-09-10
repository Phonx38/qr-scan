from rest_framework.serializers import ModelSerializer
from . import models


class QRSerializer(ModelSerializer):
    class Meta:
        model = models.ProductDetail
        fields = "__all__"
