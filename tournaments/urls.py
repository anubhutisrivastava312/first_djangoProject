from .import views
from django.urls import path,include
urlpatterns=[
    path('',views.t_home,name="t_home"),
    path('about/',views.t_about,name="t_about"),
    path('details/',views.tournamentDetail.as_view(),name="details"),
    path('sponsers/',views.sponsers,name="sponsers"),
    path('enrollment/',views.enrollment,name="enrollment"),
]