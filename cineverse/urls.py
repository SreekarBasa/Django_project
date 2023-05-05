from django.urls import path

from cineverse import views    # importing views

urlpatterns = [         # specifying the mappings i.e; the paths...
    path("", views.home, name='home'),
    path("info", views.info, name='info'),
    path("reviews", views.reviews, name='review'),
    path("about", views.timing, name='timing'),
    path("signup", views.signup, name='signup'),
    path("About_us", views.About_us, name='About_us'),
    path("Vikram", views.mov1, name='mov1'),
    path("Sita Ramam", views.mov2, name='mov2'),
    path("Thor Love and Thunder", views.mov3, name='mov3'),
]