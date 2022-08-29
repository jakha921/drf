# Django Rest Framework 

## Main installation Django and drf

- Create new project with venv
  -  `python -m venv <myvenv>`
  - check tick on main.py (PyCharm)


- Installation Django and start project
  - `pip install django-admin startproject <name> .`
  - `python manage.py runserver`


- Django migration
  - `python manage.py migrate`


- Settings
  - `LANGUAGE_CODE = 'ru-ru'`
  - `TIME_ZONE = 'Asia/Tashkent'`


- Create app
  - `python manage.py startapp <app_name>`
  - add in settings to `INSTALLED_APPS = [ <app_name>, ... ]`


- Create models and register in db
  - `class <Model_name>(models.Model): ...`
  - `python manage.py makemigrations`
  - `python manage.py migrate`

  
- Create superuser
  - `python manage.py createsuperuser`
  - register in admin.py `admin.site.register(<Model_name>)`
  - collect data and drive them in db


- Install Django Rest Framework(drf)
  -`pip install djangorestframework`
  - add in settings to `INSTALLED_APPS = [ 'rest_framework', ... ]`
  - ```
    from rest_framework import generics
    from blog.models import <Model_name>
    from blog.serializers import <Serializers_name>
    
    class MenAPIView(generics.ListAPIView):
    queryset = <Model_name>.objects.all()
    serializer_class = <Serializers_name>
    ```

- Create serializer model
  - ```
    class MenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Men
        fields = (<fields_name>, <fields_name2>, <fields_name3>, <fields_name4>)
    ```

- Urls for API
  - ```
    from blog.views import MenAPIView
    
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("api/", MenAPIView.as_view()),
    ]
      ```


- Runserver and see API
  - `http://127.0.0.1:8000/api/`