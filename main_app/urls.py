from main_app import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('finches/new', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/', views.FinchList.as_view(), name='finch_list'),
    path('finches/<int:pk>/update/',
         views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete/',
         views.FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:pk>/', views.FinchDetail.as_view(), name='finch_details'),
]
