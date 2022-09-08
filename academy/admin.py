from asyncio import events
from multiprocessing import Event
from django.contrib import admin
from .models import sport_detail,Membership_plan,Coach_Detail,Event,Member_Detail


# Register your models here.
class Admin_Coach(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Experience')#it will show data in tabular format
    search_fields=('Name','Email',)

class Admin_Sportdetail(admin.ModelAdmin):
    list_display=('Sport_name','Sport_type','Description')  
    search_fields=('Sport_type',) 

class Admin_Member(admin.ModelAdmin):
    list_display=('name','age','phone','city','plan_name')    
    search_fields=('city',)
    list_filter=['plan_name','city','age'] 


admin.site.register(sport_detail,Admin_Sportdetail)
admin.site.register(Membership_plan)
admin.site.register(Coach_Detail,Admin_Coach)
admin.site.register(Event)
admin.site.register(Member_Detail,Admin_Member)
admin.site.site_header="Sports Academy Administrations"
admin.site.site_title="Sports Admin Dashboard"
admin.site.index_title="Welcome To Our Portal"