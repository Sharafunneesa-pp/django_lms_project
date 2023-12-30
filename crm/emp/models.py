from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()
    options=(("female","female"),("male","male"))
    gender=models.CharField(max_length=100,choices=options)
    is_active=models.BooleanField(default=True)
    profilepic=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name
    


class Courses(models.Model):
    course_name=models.CharField(max_length=100,unique=True)
    duration=models.CharField(max_length=100)
    fees=models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.course_name
    

class Batches(models.Model):
    batch_name=models.CharField(max_length=200,unique=True)
    courses=models.ForeignKey(Courses,on_delete=models.CASCADE)
    options=(("yettobegin","yettobegin"),("ongoing","ongoing"),("completed","completed"))
    status=models.CharField(max_length=120,choices=options,default="yettobegin")
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)


    def __str__(self):
        return self.batch_name

# class StudentsProfile(models.Model):
#     name=models.CharField(max_length=200)
#     email=models.EmailField()
#     batch=models.ForeignKey(Batches,on_delete=models.CASCADE)
#     Phone=models.CharField(max_length=120)
#     address=models.CharField(max_length=260)
#     # options=


class MyUser(AbstractUser):
    phone=models.CharField(max_length=20)
    options=(
       ( "hr","hr"),
       ("counsellor","counsellor"),
       ("faculty","faculty"),
       ("admin","admin"),
       ("student","student"),
       ("manager","manager"),

    )
    role=models.CharField(max_length=200,choices=options,default="admin")
    opt=(
        ("male","male"),
        ("female","female"),
        ("other","other"),

    )
    gender=models.CharField(max_length=120,choices=opt,default="male")

class StudentProfile(models.Model):
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batches,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="stud_image",null=True,blank=True)
    qualification=models.CharField(max_length=200)

