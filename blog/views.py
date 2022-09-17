from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny

from blog.models import Men, Category
from blog.serializers import MenSerializer
from blog.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )    # get just by token not allowed to sessions(login from drf)


class MenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class MenAPIDestroy(generics.RetrieveDestroyAPIView):
    """get() & delete()"""
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly,)
