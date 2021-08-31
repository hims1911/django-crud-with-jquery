from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .models import ProductPublisherModels
from .serializers import ProductPublisherSerializer
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


def index(request):
	return render(request, 'PostPublisherHome/index.html')


def CreateProduct(request):
	return render(request, 'PostPublisherHome/createproduct.html')


""" API to List Product """
class ProductPublisherListAPI(generics.ListAPIView):
	#permission_classes = (IsAuthenticated,)
    template_name = "index.html"
    queryset = ProductPublisherModels.objects.all()
    serializer_class = ProductPublisherSerializer
    
    def get_queryset(self):
        queryset = self.queryset.all()
        return queryset


""" API to Create the Product """
class ProductPublisherCreateAPI(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = ProductPublisherModels.objects.all()
	serializer_class = ProductPublisherSerializer
	
	def post(self, request, *args, **kwargs):
   		generics.CreateAPIView.post(self, request, *args, **kwargs)
   		return HttpResponseRedirect('/products')



""" API to Update the Product """
class ProductRetriveUpdateDeleteApi(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = ProductPublisherModels.objects.all()
	serializer_class = ProductPublisherSerializer
	template_name = "index.html"

	def get_queryset(self):
	    queryset = self.queryset.all()
	    product_id = self.kwargs['pk']

	    print(product_id)
	    if self.request.user.is_superuser:
	        pass
	    elif product_id:
	        queryset = queryset.filter(id=product_id)

	    return queryset



