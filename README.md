# CRUD method by class (create, read, update, delete)

[drf classes to read](https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes)

```python
views.py

class MenAPIUpdate(generics.UpdateAPIView):
    """List operation"""
    queryset = Men.objects.all()
    serializer_class = MenSerializer


class MenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """CRUD operation"""
    queryset = Men.objects.all()
    serializer_class = MenSerializer
```

```python
urls.py 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.MenAPIList.as_view()),
    path('api/<int:pk>', views.MenAPIUpdate.as_view()),
    path('api/detail/<int:pk>', views.MenAPIDetailView.as_view()),
]
```

```python
settings.py

REST_FRAMEWORK = {
    # Control dfr permission & etc globally
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',

        # get in comment when project give to realise
        'rest_framework.renderers.BrowsableAPIRenderer',    # give permission for to browser for CRUD
    ],
}

```