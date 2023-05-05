from django.urls import path, include

from signup import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
]