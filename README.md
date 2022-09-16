# ViewSet CRUD

[ViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#custom-viewset-base-classes)<br />
[Router](https://www.django-rest-framework.org/api-guide/routers/#simplerouter)

```python
views.py

class MenViewSet(viewsets.ModelViewSet):    # ReadOnlyModelViewSet get()
    # ModelViewSet include > mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet
    """ CRUD all by one class """
    queryset = Men.objects.all()
    serializer_class = MenSerializer
```

```python
urls.py 

router = routers.SimpleRouter()
router.register(r'', views.MenViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))  # http://127.0.0.1:8000/api/{router_url}


    # path('api/', views.MenViewSet.as_view({'get': 'list'})),    # enter method in as_view()
    # path('api/<int:pk>', views.MenViewSet.as_view({'put': 'update'})),
]

]
```
