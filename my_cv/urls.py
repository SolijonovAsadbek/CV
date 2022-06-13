from django.urls import path

from my_cv import views

urlpatterns = [
    path('', views.HeadClass.as_view(), name='head')
]
