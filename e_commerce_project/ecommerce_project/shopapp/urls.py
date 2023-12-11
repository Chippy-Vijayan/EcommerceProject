from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
app_name='shopapp'
urlpatterns = [
    path('',views.allProductCat,name='allProductCat'),
    path('<slug:c_slug>/',views.allProductCat,name='products_by_category'),
    path('<slug:c_slug>/,<slug:product_slug>/', views.productDetail, name='productCategoryDetail'),

]