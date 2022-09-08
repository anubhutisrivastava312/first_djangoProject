from django.shortcuts import render,HttpResponse
from django.views import View

from academy.models import Gender
from .models import Enrollment, Tournament
from django.contrib import messages

# Create your views here.
def t_home(request):
    # return HttpResponse("<h1>This is tournament home page</h1>")
    return render(request,'tournaments/html/tournament_home.html')

def t_about(request):
    return HttpResponse("<h1> this is about us page</h1>")

class tournamentDetail(View): #class based view= used to make the code and use for custom methods
    def get(self,request):
        t_queryset=Tournament.objects.all()
        t_dict={
            "t_data":t_queryset
        }
        return render(request,'tournaments/html/tournament_detail.html',t_dict)


def sponsers(request):
    return render(request,'tournaments/html/sponsers.html')


def enrollment(request):
    if request.method=="GET":
        t_objects=Tournament.objects.all()
        tournament_dict={
            "t_key":t_objects
        }
        return render(request,'tournaments/html/enrollment.html',tournament_dict)

    if request.method=="POST":
        name=request.POST["txtname"]    
        age=request.POST["txtage"]
        email=request.POST["txtemail"]
        phone=request.POST["txtphone"]
        city=request.POST["cmbcity"]
        address=request.POST["txtaddress"]
        tournament_name=request.POST["tournament_name"]
        gender=request.POST["gender"]

    if int(age)<18 or int(age)>60:
        messages.error(request,"your age should be between 18 to 60")
        return render(request,'tournaments/html/enrollment.html')
    elif len(phone)>10 or len(phone)<10 or int(phone)<0:
        messages.error(request,"invalid phone number")
        return render(request,'tournaments/html/enrollment.html')    
    else:
        new_member=Enrollment(name=name,age=age,email=email,phone=phone,city=city,address=address,tournament_name=tournament_name,Gender=gender)    
        
        
    new_member.save()
    print("Member enrolled successfully")
    messages.success(request,"Thankyou for enrolling")
    return render(request,'tournaments/html/enrollment.html')


