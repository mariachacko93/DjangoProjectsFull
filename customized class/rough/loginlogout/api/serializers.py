from rest_framework.serializers import ModelSerializer
from loginout.models import LoginModel

class Loginserializer(ModelSerializer):
    class Meta:
        model=LoginModel
        fields=["username","password"]
