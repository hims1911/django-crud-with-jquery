from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index),
	path('createproduct', views.CreateProduct),
	path('api/showproducts/', views.ProductPublisherListAPI.as_view()),
	path('api/createproduct', views.ProductPublisherCreateAPI.as_view(), name="create-product"),
	path('api/productupdate/<int:pk>', views.ProductRetriveUpdateDeleteApi.as_view())
]
