from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny

from blog.models import Men, Category
from blog.serializers import MenSerializer
from blog.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class MenAPIListPagination(PageNumberPagination):
    page_size = 3   # show given el in one page
    page_size_query_param = 'page_size'
    max_page_size = 10000


class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = MenAPIListPagination
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
