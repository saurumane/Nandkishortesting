from django.contrib import admin

# Register your models here.

from.models import UserModel
class UserAdmin(admin.ModelAdmin):
    List_Display=['id','username','usercity','useremail','userphone']

admin.site.register(UserModel,UserAdmin)