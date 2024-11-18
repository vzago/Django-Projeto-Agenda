from django.urls import path
from contact import views

#Name Space

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]
