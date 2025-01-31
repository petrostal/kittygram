# # Обновлённый views.py
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# from rest_framework import generics


# from .models import Cat
# from .serializers import CatSerializer


# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# # class APICat(APIView):
# #     def get(self, request):
# #         cats = Cat.objects.all()
# #         serializer = CatSerializer(cats, many=True)
# #         return Response(serializer.data)

# #     def post(self, request):
# #         serializer = CatSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # class APICatDetail(APIView):
# #     def get(self, request, pk):
# #         # pk = self.kwargs['pk']
# #         cat = Cat.objects.get(pk=pk)
# #         serializer = CatSerializer(cat)
# #         return Response(serializer.data)

# #     def put(self, request, pk):
# #         # pk = self.kwargs['pk']
# #         cat = Cat.objects.get(pk=pk)
# #         serializer = CatSerializer(cat, data=request.data, partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         # pk = self.kwargs['pk']
# #         cat = Cat.objects.get(pk=pk)
# #         cat.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)

# #     def patch(self, request, pk):
# #         return self.put(request, pk)


# views.py
from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
