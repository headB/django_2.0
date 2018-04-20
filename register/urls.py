from django.conf.urls import url
from django.urls import path,re_path
from register import views
urlpatterns = [

    ##通过url函数设置url路由配置项
    #url(r'^index',views.index),
    path('book/<int:number>/',views.index),
    #path(r'book/<int:number>/',views.index)
    ##name的作用,用于重定向?
    ##
]