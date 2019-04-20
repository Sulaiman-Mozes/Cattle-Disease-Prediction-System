from rest_framework import serializers
from information.models import Disease

 
class DiseaseSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Disease
        fields = [
            'uri',
            'pk',
            'disease',
            'description',
            'causes',
            'symptoms',
            'treatment',
            'prevention',
            'timestamp',
        ]
        read_only_fields = ['pk']

    def get_uri (self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)