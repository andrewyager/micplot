from django.urls import path, include, re_path
from . import views

app_name = "cast"
urlpatterns = [
    re_path("castlist/<int:run_id>/", views.cast_list, name="castlist"),
    re_path(
        "characterlist/<int:run_id>/",
        views.character_list,
        name="characterlist",
    ),
    re_path(
        "characterlist/<int:run_id>/wavetool/",
        views.cast_export,
        name="characterlistwavetool",
    ),
]
