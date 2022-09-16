from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from blog.models import Men, Category
from blog.serializers import MenSerializer


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
