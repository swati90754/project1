from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    list_display = ('id','username','password','first_name','last_name','email','landmark','address','city','country','state')
    
   

admin.site.register(User, UserAdmin)
