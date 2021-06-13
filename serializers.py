from rest_framework import serializers

from api_dec.models import Job


class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

