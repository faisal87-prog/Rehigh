from django.urls import path
from . import views

urlpatterns = [

    path('blogs/', views.blog_list),
    path('blogs/<int:pk>/', views.blog_detail),
    path('swipers/', views.swiper_list),
    path('swipers/<int:pk>/', views.swiper_detail),
    path('appointments/', views.appointment_list),
    path('appointments<int:pk>', views.appointment_detail),
    path('variations/', views.variation_list),
    path('variations<int:pk>', views.variation_detail)

]