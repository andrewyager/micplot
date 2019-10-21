from django.urls import path, include
from django.conf.urls import url
from . import views

app_name='cast'
urlpatterns = [
	path('castlist/<int:run_id>/', views.cast_list, name='castlist'),
	path('characterlist/<int:run_id>/', views.character_list, name='characterlist'),
	path('characterlist/<int:run_id>/wavetool/', views.cast_export, name='characterlistwavetool'),
]
