from .views import home, about_us, contact_us

from django.urls import path, include

urlpatterns = [
    path('', home, name="home"),
    path('about-us', about_us, name="about"),
    path('contact-us', contact_us, name="contact"),
]
