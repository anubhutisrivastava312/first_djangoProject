import email
from django.shortcuts import render,HttpResponse,redirect
from .models import Coach_Detail, Feedback, Membership_plan, sport_detail,Contact ,Event ,Member_Detail#because we have to access the sport_detail from the models.py to fetch the data for sportsdetails
from django.contrib import messages
# Create your views here.

def home(request):
    event_objects=Event.objects.all()
    event_dict={
        "event_key":event_objects
    }
    
    return render(request,'academy/html/index.html',event_dict)


def contactus(request):
    if request.method=="POST":         #request.POST is dictionary and control names are keys here
        user_name=request.POST["txtname"]
        user_email= request.POST["txtemail"]
        user_phone= request.POST["txtphone"]
        user_query=request.POST["txtquery"]
        c=Contact(name=user_name, email=user_email,phone=user_phone, your_query=user_query)# object creation
        c.save() #ORM CONCEPT(saving the object and it will store the data submitted through contact form in the database)
        print("contact saved successfully")
        messages.success(request,"Thank you for contacting us we will reach you soon")
        return render(request,'academy/html/contactus.html')
        

    

    return render(request,'academy/html/contactus.html')


def aboutus(request):
    return render(request,'academy/html/aboutus.html')

def feedback(request):
     if request.method=="POST":         
        user_name=request.POST["txtname"]
        user_feedback= request.POST["txtfeedback"]
        user_rating= request.POST["cmbrating"]
        
        f=Feedback(name=user_name, feedback=user_feedback,rating=user_rating)
        f.save() 
        print("feedback saved successfully")
        messages.success(request,"Thank you for your feedback")
        return render(request,'academy/html/feedback.html')
        
     return render(request,'academy/html/feedback.html')    

#to show the details of all sports
def sports(request):
    sports_objects=sport_detail.objects.all()#it returns the query set which is a collection of objects.it will return all the rows from the table sports_details
    
    #to show the data on the template page or send the data on the html page from view

    sports_dict={
        "sports_data":sports_objects,  #this is the only way to show the data on the html page..we have to make a dictionary variable and bind it with the variable containing the collection of objects(sports_objects) 
    }

    return render(request,'academy/html/allsports.html',sports_dict)#to send the data (render)


def membership_plans(request):
    plan_objects=Membership_plan.objects.all()
    plan_dict={

        "plan_data":plan_objects,
    }  
    return render(request,'academy/html/plan_show.html',plan_dict) 


def coach_details(request):
    coach_objects= Coach_Detail.objects.all()   
    coach_dict={

        "coach_data":coach_objects,

    }
    return render(request,'academy/html/coachdata_show.html',coach_dict)



def registration(request):
    if request.method=="GET":
        plan_objects=Membership_plan.objects.all()
        plan_dict={"plan_key":plan_objects}
        return render(request,'academy/html/registration.html',plan_dict)

    
    if request.method=="POST":
        member_id=request.POST["txtuserid"]
        member_pass=request.POST["txtuserpass"]
        member_name=request.POST["txtname"]
        member_phone=request.POST["txtphone"]
        member_address=request.POST["txtaddress"]
        member_city=request.POST["cmbcity"]
        member_gender=request.POST["gender"]
        member_age=request.POST["txtage"]
        member_transaction=request.POST["txttransaction"]
        member_plan_name=request.POST["cmb_plan"]
        #len(member_age)>2 or int(member_age)<0
        if int(member_age)<18 or int(member_age)>=60:
            messages.error(request,"your age should be between 18 to 60")
            return render(request,'academy/html/registration.html')
        elif len(member_phone)>10 or len(member_phone)<10 or int(member_phone)<0:
            messages.error(request,"please enter a valid phonr number")
            return render(request,'academy/html/registration.html')   

        else:
            new_member=Member_Detail(member_id=member_id,password=member_pass,name=member_name,age=member_age,phone=member_phone,city=member_city,address=member_address,gender=member_gender,plan_name=member_plan_name,
        transaction_no=member_transaction)
        
        
        new_member.save()
        print("member registered successfully")
        messages.success(request,"Thankyou for being a Member")
        return render(request,'academy/html/registration.html')

def member_login(request):
    if request.method=="GET":
     return render(request,'academy/html/login.html')

    if request.method=="POST":
        mem_id=request.POST["userid"] 
        mem_password=request.POST["userpass"]
        member_query_set=Member_Detail.objects.filter(member_id=mem_id,password=mem_password)
        print(len(member_query_set))
        if len(member_query_set)==1:
            request.session["member_session"]=mem_id#built in dict (session)
            member_object={
                "member_data":member_query_set
            }

            return render(request,'academy/html/member/member_home.html',member_object)
        else:
            messages.error(request,'Invalid UserID/Password')
            return render(request,'academy/html/login.html')

def member_editprofile(request):
    if "member_session" not in request.session.keys():
        return redirect("member_login")


    if request.method=="GET":
        loggedIn_member_ID=request.session["member_session"] #fetching values from session
        member_object=Member_Detail.objects.get(member_id=loggedIn_member_ID)#finding the object
        member_dict={
            "member_data":member_object
        }
        return render(request,'academy/html/member/member_editprofile.html',member_dict)     


    if request.method=="POST":
        ph=request.POST["phone"]   
        add=request.POST["address"]
        loggedIn_member_ID=request.session["member_session"]#fetching values from session
        member_object=Member_Detail.objects.get(member_id=loggedIn_member_ID)
        member_dict={
            "member_data":member_object
        }  
        member_object.phone=ph#setting the new values in the variables of MemberDetail
        member_object.address=add
        member_object.save()#save the changes for the MemberDetail Object
        messages.success(request,"Profile updated successfully")      
        return render(request,'academy/html/member/member_editprofile.html',member_dict)


def member_logout(request):
    if "member_session" not in request.session.keys():
        return redirect("member_login")

    del request.session["member_session"] #it is used to destroy the session
    return redirect(member_login)


##<----------------for member view profile---------->####
def member_view_profile(request):

    if "member_session" not in request.session.keys():
        return redirect("member_login")

    if request.method=="GET":
        loggedIn_member_ID=request.session["member_session"]
        member_object=Member_Detail.objects.get(member_id=loggedIn_member_ID)
        member_dict={
            "member_data":member_object
        }
        return render(request,'academy/html/member/member_view_profile.html',member_dict)