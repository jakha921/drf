from django.forms import model_to_dict
from rest_framework import generics, viewsets

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Men
from blog.serializers import MenSerializer


class MenViewSet(viewsets.ModelViewSet):    # ReadOnlyModelViewSet get()
    # ModelViewSet include > mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet
    """ CRUD all by one class """
    queryset = Men.objects.all()
    serializer_class = MenSerializer

# class MenAPIList(generics.ListCreateAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer
#
#
# class MenAPIUpdate(generics.UpdateAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer
#
#
# class MenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer
#
