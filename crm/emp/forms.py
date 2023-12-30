from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
# class EmployeeForm(forms.Form):
#     name=forms.CharField()
#     dept=forms.CharField()
#     salary=forms.FloatField()
#     gender=forms.CharField()
#     profilepic=forms.ImageField()


from emp.models import Employee,Courses,Batches,StudentProfile,MyUser
from django.contrib.auth.models import User
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        # fields=['name','dept','salary','gender','profilepic']
        # we want to passs it as tuple. so put , after that either considered as string
        exclude=("is_active",)
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "dept":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "gender":forms.Select(attrs={"class":"form-select"}),
            "profilepic":forms.FileInput(attrs={"class":"form-control"})

        }



class RegistrationForm(forms.ModelForm):
    class Meta:
        model=MyUser
        fields=["first_name","last_name","username","email","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})

        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None  # Corrected field access
        
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Using set_password to hash the password
        if commit:
            user.save()
        return user   
      

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class AdminLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))


class CourseForm(forms.ModelForm):
    class Meta:
        model=Courses
        exclude=("is_active",)
       

class BatchForm(forms.ModelForm):
    class Meta:
         model=Batches
         exclude=("status","end_date")
         widgets={
            "batch_name":forms.TextInput(attrs={"class":"form-control"}),
            "courses":forms.Select(attrs={"class":"form-control form select"}),
            "start_date":forms.DateInput(attrs={"class":"form_control","type":"date"})  
         }

class UserProfileForm(UserCreationForm):
     class Meta:
        model = MyUser
        fields = ["first_name","email","username","password1","password2","phone","role","gender"]

class StudentProfileForm(forms.ModelForm):
    
    class Meta:
        model = StudentProfile
        exclude=("user",)
       









