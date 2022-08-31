from django.forms import model_to_dict
from rest_framework import generics

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Men
from blog.serializers import MenSerializer


# Create your views here.
# class MenAPIView(generics.ListAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer


class MenAPIView(APIView):
    def get(self, request):
        m_model = Men.objects.all()
        return Response({'posts': MenSerializer(m_model, many=True).data})

    def post(self, request):
        """Check form is valid & send msg"""
        serializer = MenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Men.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id'],
        )
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Put not allowed"})

        try:
            instance = Men.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = MenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Men.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = MenSerializer(instance=instance)
        return Response({"post": "delete post " + str(pk)})