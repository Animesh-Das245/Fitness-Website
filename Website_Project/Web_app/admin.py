from django.contrib import admin
from .models import Appointment
from .models import Profile

admin.site.register(Appointment)
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone_number','email_verified','uuid']

# Register your models here.
