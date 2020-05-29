from django.urls import path
from . import views
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView)

urlpatterns = [
    path('', views.home,name='home'),
    path('home/',ProductListView.as_view()),
    path('home/<int:pk>/',ProductDetailView.as_view(),name='detail'),
    path('home/<int:pk>/update/',ProductUpdateView.as_view(),name='update'),
    path('new/',ProductCreateView.as_view(),name='create'),
    path('about/',views.about,name='about'),
    path('home/<int:pk>/delete',ProductDeleteView.as_view(),name='delete'),
]
