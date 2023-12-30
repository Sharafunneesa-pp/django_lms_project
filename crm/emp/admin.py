from django.contrib import admin

# Register your models here.
from emp.models import MyUser
admin.site.register(MyUser)
