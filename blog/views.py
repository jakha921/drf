from rest_framework import generics

from django.shortcuts import render

from blog.models import Men
from blog.serializers import MenSerializer


# Create your views here.
class MenAPIView(generics.ListAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
