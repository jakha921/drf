# Pagination

[Pagination](https://www.django-rest-framework.org/api-guide/pagination/)<br />



```python
settings.py

REST_FRAMEWORK = {
    ...
    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 3,
```

```python
views.py

from rest_framework.pagination import PageNumberPagination


class MenAPIListPagination(PageNumberPagination):
    page_size = 3   # show given el in one page
    page_size_query_param = 'page_size' # edit page size > url&page_size=4
    max_page_size = 10000


class MenAPIList(generics.ListCreateAPIView):
    ...
    pagination_class = MenAPIListPagination
  
```
