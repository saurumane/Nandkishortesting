from django.shortcuts import render
from .models import UserModel
# Create your views here.
from .forms import UserForm
from django.db.models import Avg,Sum,Count,Min,Max
from django.http import HttpResponseRedirect
def userview(r):
    user_list=UserModel.objects.all()
    #user_list=UserModel.objects.filter(id__gte=105)
    #user_list=UserModel.objects.filter(usercity__exact='mumbai')
   # user_list=UserModel.objects.filter(username__contains="a")
    #user_list=UserModel.objects.filter(username__icontains="a")  #this is not case sensitive
    #user_list=UserModel.objects.filter(id__in=[102,119,19,1,108])
    #user_list=UserModel.objects.filter(username__istartswith='m')   #i becomes case sinensitive
    #user_list=UserModel.objects.filter(useremail__iendswith='rediff.com')
   # user_list=UserModel.objects.filter(userphone__endswith=9)
   # user_list=UserModel.objects.filter(id__range=[100,105])

    #user_list=UserModel.objects.filter(id__gt=100) or UserModel.objects.filter(usercity__exact='Mumbai')  #only one should be satisfied
   # user_list=UserModel.objects.exclude(id=110)
   # user=UserModel.objects.all().aggregate(Max('id'))
   # user_list=UserModel.objects.all().order_by('id')
    user_list=UserModel.objects.all().order_by('-id')[0:1]

    return render(r,'users/userinfo.html',{'user_list':user_list})
    #return render(r,'users/agg.html',{'user':user})
def user_form(r):
    form=UserForm()
    if r.method=='POST':
        form=UserForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/info')
    return render(r,'users/userform.html',{'form':form})


def user_delete(r,id):
    user=UserModel.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect('/user/info')

def user_update(r,id):
    user=UserModel.objects.get(id=id)
    if r.method=='POST':
        form=UserForm(r.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/info')
    return render(r,'users/updateinfo.html',{'user':user})


