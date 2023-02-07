from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_view),
    path('start', views.start_view),
    path('login', views.login_view, name = 'login'),
    path('join', views.join_view, name = 'join'),
    path('main', views.main_view, name = 'main'),
    path('lrooms', views.lrooms_view, name = 'lrooms'),
    path('drooms', views.drooms_view, name = 'drooms'),
    path('prooma', views.prooma_view, name = 'prooma'),
    path('proomb', views.proomb_view, name = 'proomb'),
    path('brooma', views.brooma_view, name = 'brooma'),
    path('broomb', views.broomb_view, name = 'broomb'),
    path('vrooma', views.vrooma_view, name = 'vrooma'),
    path('vroomb', views.vroomb_view, name = 'vroomb'),
    path('hllwys', views.hllwys_view, name = 'hllwys')
]

