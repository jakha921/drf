from rest_framework import viewsets, generics
from rest_framework.decorators import permission_classes

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny

from blog.models import Men, Category
from blog.serializers import MenSerializer
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
