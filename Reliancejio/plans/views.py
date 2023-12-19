from django.shortcuts import render
from .models import PlansModel
from django.contrib.auth.decorators import login_required



@login_required
def prepaid(r):
    plan_list=PlansModel.objects.all()
    return render(r,'plans/prepaid.html',{'plan_list':plan_list})
