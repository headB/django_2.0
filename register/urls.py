from django.conf.urls import url
from django.urls import path
from register import views
urlpatterns = [

    ##通过url函数设置url路由配置项
    #url(r'^index',views.index),
    path('',views.index,name='index')
]