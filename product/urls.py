from django.urls import path
from . import views

urlpatterns = [
    # ex: /product/
    path('', views.product, name='product'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.product_by_category, name='product_by_category'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
]
