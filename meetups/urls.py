from django.urls import path
from meetups import views

urlpatterns = [
    path('',views.meetup_list, name = 'meetup-list'),
    path('<slug:meetup_slug>/confirmation',views.confirmation, name = 'confirmation'),
    path('<slug:meetup_slug>',views.meetup_detail, name = 'meetup-detail'),
]