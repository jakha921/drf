# CRUD method by class (create, read, update, delete)

[drf classes to read](https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes)

```python
views.py

class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
```

```python 
serializers.py

class MenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Men
        fields = ('title', 'content', 'is_published',)

```

```python
urls.py 

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.MenAPIList.as_view()),
    path('api/<int:pk>', views.MenAPIView.as_view()),
]
```