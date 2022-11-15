from django.shortcuts import render
from .models import Descuentos
from .serializers import DescuentosSerializer
from rest_framework import  viewsets
# Create your views here.


class DescuentosViewSet(viewsets.ModelViewSet):
    serializer_class = DescuentosSerializer

    def get_queryset(self):
        coupons = Descuentos.objects.all()
        return coupons