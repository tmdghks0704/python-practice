from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),
    path('user_creative/', views.user_creative),
    path('user_new/', views.user_new),
    path('throw/', views.throw),
    path('get/', views.get),
    path('result/', views.result),
    path('catch/', views.catch),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('template_example/', views.template_example),
    path('isbirth/', views.isbirth),
    path('area/<int:r>/', views.area),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('dlsk/<name>/<int:age>/', views.dlsk),
    path('cube/<int:num>/', views.cube),
    path('hello/<name>/', views.hello),
    # path('home/lottos1/', views.lottos1),
    path('dinner/', views.dinner),
    path('lotto/', views.lotto),
    path('midnight/', views.midnight),
    path('hola/', views.hola),
    path('index/', views.index),
    ]