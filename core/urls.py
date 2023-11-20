from django.urls import path
from .views import ClienteViewSet

urlpatterns = [
    path('', ClienteViewSet.as_view({'get': 'list','post':'create'}), name='teste'),
]
