from django.urls import include, path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.register),
    path('login/', views.LoginView.as_view()),
    path('refresh/', views.LoginView.as_view()),
]
