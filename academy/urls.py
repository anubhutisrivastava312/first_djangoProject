from django.urls import path,include
from .import views 

urlpatterns = [
   
  path("",views.home,name="home"),
  path("contactus/",views.contactus,name="contactus"),
  path("aboutus/",views.aboutus,name="aboutus"),
  path("feedback/",views.feedback,name="feedback"),
  path("sportsdetails/",views.sports,name="sports_details"),
  path("membership_plans/",views.membership_plans,name="membership_plans"),
  path("coach_details/",views.coach_details,name="coach_details"),
  path('member_registration/',views.registration,name="member_registration"),
  path('member_login/', views.member_login, name="member_login"),
  path('member_editprofile/',views.member_editprofile,name="member_editprofile"),
  path('member_logout/',views.member_logout,name="member_logout"),
  path('member_view_profile/',views.member_view_profile,name="member_view_profile"),


]
