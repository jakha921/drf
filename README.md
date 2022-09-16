# ViewSet CRUD

[ViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#custom-viewset-base-classes)<br />
[Router](https://www.django-rest-framework.org/api-guide/routers/#simplerouter)

```python
views.py

class MenViewSet(viewsets.ModelViewSet):  # ReadOnlyModelViewSet get()
    """ CRUD all by one class """
    # queryset = Men.objects.all()
    serializer_class = MenSerializer

    def get_queryset(self):
        """return just given numb of el"""
        pk = self.kwargs.get('pk')
        if not pk:
            last = (len(Men.objects.all()))-3
            return Men.objects.all()[last:]
        
        return Men.objects.filter(pk=pk)

    @action(methods=["GET"], detail=True)      # http://127.0.0.1:8000/api/category/   detail return one element
    def category(self, request, pk):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

```

```
urls.py 

DefaultRouter > show all urls which router
    router = routers.DefaultRouter()
    
    {
        "men": "http://127.0.0.1:8000/api/men/"
    }

SimpleRouter > show just API without routering

    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

router = routers.SimpleRouter()
router.register(r'', views.MenViewSet, basename='men')  # basename need when in ModelViewSet not use queryset(model)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))  # http://127.0.0.1:8000/api/{router_url}
]


```
