from django.urls import path
from . import views #import views


# adding url
urlpatterns = [
    path('', views.index, name='home'), #home
    path('portfolio', views.portfolio, name='portfo'), #portfolio
    path('resume', views.resume, name='resume'), #resume
    #path('contact', views.contact, name='contact'), #contact
]