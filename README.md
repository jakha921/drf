# Show how work serialization

+ In views.py write this code 
```
class MenAPIView(APIView):
    def get(self, request):
    """ get request object """
        # return Response({'title': 'Bread Peat'})
        lst = Men.objects.all().values()
        return Response(lst)

    def post(self, request):
    """ post request object """
        post_new = Men.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id'],
        )
        return Response({'post': model_to_dict(post_new)})
```

