from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='barrowman_equations'),
    path('eq',views.eq,name='eq result')
]