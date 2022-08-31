import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from blog.models import Men


# class MenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class MenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateField(read_only=True)
    time_update = serializers.DateField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()


# def encode():
#     model = MenModel("Jali", "Angilen")
#     model_sr = MenSerializer(model)
#     print(model_sr, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Angelina Jolie", "content": "Contetnt: Anjelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = MenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)