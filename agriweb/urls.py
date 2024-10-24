from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('supplier', supplier, name="supplier"),
    path('blog', blog, name="blog"),
    path('contact', contact, name="contact"),
    path('farmer/contact', farmercontact, name="farmercontact"),
    path('subscribe', subscribe, name="subscribe"),
]
