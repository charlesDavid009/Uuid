from .views import HomeView
from django.urls import path

urlpatterns = [
    path('uuid/', HomeView.as_view()),
]
