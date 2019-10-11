from django.urls import path, include
from django.conf.urls import url
from . import views

app_name='show'
urlpatterns = [
	path('<int:show_id>/<int:run_id>/songs/', views.song_detail_list),
]
