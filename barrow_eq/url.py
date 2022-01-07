from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [

    path('',views.home,name='barrowman_equations'),
    path('eq',views.eq,name='eq result')
]

urlpatterns += staticfiles_urlpatterns()