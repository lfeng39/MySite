from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('detail',views.detail, name='detail'),
    path('img',views.img, name='img'),
    path('lib',views.lib, name='lib'),
    path('toys',views.toys, name='toys'),
]