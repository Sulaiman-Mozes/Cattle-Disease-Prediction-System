from rest_framework import generics, permissions
from information.models import Disease
from .serializers import DiseaseSerializer


class DiseasesEndpoint(generics.ListCreateAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class DiseaseEndpoint(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request} 