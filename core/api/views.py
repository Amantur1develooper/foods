from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Foods
from .serializers import FoodsSerializer

class FoodsListCreateView(generics.ListCreateAPIView):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer

class FoodsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer
    
@api_view(['POST'])
def clear_count_foods(request):
    Foods.objects.filter(count__gt=0).update(count=0)
    return Response(status=status.HTTP_204_NO_CONTENT)
