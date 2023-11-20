from rest_framework import viewsets
from .serializers import ClienteSerializer
from .models import Cliente
# Create your views here.
# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer