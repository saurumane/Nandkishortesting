from django.contrib import admin
from .models import PlansModel
# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = ['planid','planname','plandetails','planamount']
admin.site.register(PlansModel,PlanAdmin)
