from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload_resume, name="upload"),
    path("result/<int:resume_id>/", views.result, name="result"),
    path("dashboard/", views.dashboard, name="dashboard"),
]