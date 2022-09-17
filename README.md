# Djoser auth

[Djoser](https://djoser.readthedocs.io/en/latest/index.html)<br />
[Base Endpoints](https://djoser.readthedocs.io/en/latest/base_endpoints.html#base-endpoints)



```python
settings.py

pip install djoser  # install command 

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
]

python manage.py migrate    # command migrate

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',    # djoser
        'rest_framework.authentication.BasicAuthentication',    # default settings
        'rest_framework.authentication.SessionAuthentication',  # default settings
    ]
}

```

```python
views.py

class MenAPIList(generics.ListCreateAPIView):
    ...
    # get just by token not allowed to sessions(login from drf)
    authentication_classes = (TokenAuthentication, )    
```


```python
urls.py 

urlpatterns = [
    ...
    # auth url for logining on drf (give token by session)
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # url/auth/token/login/
    # re_path(r'^auth/', include('djoser.urls.jwt')),         # JWT auth
]
```

```python
# create user by Base Endpoints(on header)
# send username, password & email to url below for registration user
url/auth/users/

# to take a token send username & password to url below
auth/token/login/
# return token for using

# for destroying token send Authorization Token {token} to url below
/auth/token/logout/

```