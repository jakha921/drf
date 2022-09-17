# Swagger autodocumentation

[drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html#usage)<br />



```python
pip install drf-yasg

settings.py

INSTALLED_APPS = [
   ...
   'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
   'drf_yasg',
   ...
]
```

```python
drf_yasg.py

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Men API",
        default_version='',
        description="Men`s API documentation\n<code>/redoc</code> another docs",
        contact=openapi.Contact(name='Jakha921'),
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticated],
)

urlpatterns = [
    path('docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),    # download documentation in some format
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),   # documentation
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),         # another documentation
]  
```

```python
url.py

from .drf_yasg import urlpatterns as doc_urlpatterns

urlpatterns += doc_urlpatterns
```