# Permission class & custom permissions

[Permission](https://www.django-rest-framework.org/api-guide/permissions/)

```python
models.py

from django.contrib.auth.models import User

class Men(models.Model):
    ...
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
```

```python
views.py

from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class MenAPIList(generics.ListCreateAPIView):
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """return just given numb of el"""
        last = (len(Men.objects.all())) - 3
        return Men.objects.all()[last:]


class MenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class MenAPIDestroy(generics.RetrieveDestroyAPIView):
    """get() & delete()"""
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly,)

```

```python
permissions.py

from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

```

```python
serializers.py

class MenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Men
        fields = '__all__'

```


```python
urls.py 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.MenAPIList.as_view()),
    path('api/<int:pk>/', views.MenAPIUpdate.as_view()),
    path('api/delete/<int:pk>/', views.MenAPIDestroy.as_view()),
]
```

```python

global permission

REST_FRAMEWORK = {
    ...
    
    # global permissions. If you give permission in permission classes than will work.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```
