# CRUD method (create, read, update, delete)


```python
views.py

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
```

```python 
serializers.py

class MenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateField(read_only=True)
    time_update = serializers.DateField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Men.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.save()
        return instance

    def delete(self, instance):
        return Men.objects.delete(inst
```

```python
urls.py 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', MenAPIView.as_view()),
    path('api/<int:pk>', MenAPIView.as_view()),
]
```