# JWT auth

[JWT Simple](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation)<br />
[Simple JWT’s settings](https://django-rest-framework-simplejwt.readthedocs.io/en/stable/settings.html)



```python
settings.py

pip install djangorestframework-simplejwt  # install command 


REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',    # JWT
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
    # authentication_classes = (TokenAuthentication, )    
```


```python
urls.py 

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   # JWT refresh token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),      # JWT verify token
]
```

```python
settings.py

# JWT settings get all and past
# JWT Token is include HEADER.PAYLOAD.VERIFY-SIGNATURE

# Django project settings.py

from datetime import timedelta
...

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # time of updating
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',   # Encoding to HS256
    'SIGNING_KEY': SECRET_KEY,  # Use as SIGNING_KEY(VERIFY-SIGNATURE)
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),   # # Authorization: Bearer {token}
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',     # show user as "user_id": 1
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
```