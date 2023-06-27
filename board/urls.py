from django.urls import path

from board import views


urlpatterns = [
    path("main", views.MainView.as_view(), name="main"),
]
