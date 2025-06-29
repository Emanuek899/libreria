from django.urls import path
from . import views

utlpatterns = [
	path('', views.render_index, name='index'),
]