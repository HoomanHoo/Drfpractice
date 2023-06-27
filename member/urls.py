from django.urls import path

from member import views

urlpatterns = [
    path("login-page", views.LoginView.as_view(), name="login"),
    path("regist-page", views.RegistView.as_view(), name="regist"),
]
