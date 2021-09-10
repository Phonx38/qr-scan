from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

# Create your views here.

class ProductList(APIView):
    serializer_class = serializers.QRSerializer

    def get(self, request, format=None):
        products = models.ProductDetail.objects.all()
        serializer = serializers.QRSerializer(products, many=True)
        return Response(serializer.data)

class QRAdd(APIView):

    serializer_class = serializers.QRSerializer


    def post(self, request):

        serializer = serializers.QRSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "message": "Success", "Data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "message": "Error"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class QRDetail(APIView):
    def get_object(self, pk):
        try:
            return models.ProductDetail.objects.get(pk=pk)
        except ProductDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = serializers.QRSerializer(product)
        print(product.qr_code.url)
        return Response(serializer.data)
