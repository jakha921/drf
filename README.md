# Serializer in details & return valid error

+ Serializer mock test models

```python
class MenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class MenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = MenModel("Jali", "Angilen")
    model_sr = MenSerializer(model)
    print(model_sr, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"title": "Angelina Jolie", "content": "Contetnt: Anjelina Jolie"}')
    data = JSONParser().parse(stream)
    serializer = MenSerializer(data=data)
    serializer.is_valid()
    print(serializer.valid
```


```shell
    python manage.py shell
    from <app_name>.serializer import decode
    decode()
    
    OrderedDict([('title', 'Angelina Jolie'), ('content', 'Contetnt: Anjelina Jolie')])
    
    quit()
```

+ modify serializers.py & work with models

```python 
serializers.py

class MenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateField(read_only=True)
    time_update = serializers.DateField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()
```

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
        return Response({'post': MenSerializer(post_new).data})
```

check localhost