from django.shortcuts import render

from .forms import SignupForm
from django.http import HttpResponseRedirect
def index(r):
    return render(r,'home/index.html')


def signup_view(r):
    form=SignupForm()
    if r.method=='POST':
        form=SignupForm(r.POST)
        user=form.save()
        user.set_password(user.password) #normal text to encrypted
        user.save()
        return HttpResponseRedirect('/')


    return render(r,'home/signup.html',{'form':form})