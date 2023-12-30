from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from emp.forms import EmployeeForm,RegistrationForm,LoginForm,CourseForm,AdminLoginForm,RegistrationForm,BatchForm,StudentProfileForm,UserProfileForm
from emp.models import Employee,Courses,Batches,MyUser,StudentProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required



# Create your views here.

# @method_decorator(login_required(login_url='signin'), name='dispatch')
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class IndexView(TemplateView):

    template_name="index.html"

# @method_decorator(login_required(login_url='signin'), name='dispatch')
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeForm()
        return render(request,"emp_add.html",{"form":form})

    def post(self,request,*args,**kwargs):
        # form=EmployeeForm(request.POST)
        # files=request.Files should be given if there is image
        form=EmployeeForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee has been added")
            return redirect("emp_list")   
        else:
            messages.error(request,"Employee creation failed")
            return render(request,"emp_add.html",{"form":form})    


# @method_decorator(login_required(login_url='signin'), name='dispatch')       
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,"emp_list.html",{"employee":qs})
    
# class EmployeeListView(ListView):
#     model=Employee
#     template_name='emp_list.html'
#     context_object_name="employee"


# @method_decorator(login_required(login_url='signin'), name='dispatch')    
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        # kwargs={id:1}
        # id=kwargs.get('id')
        id=kwargs.get('pk')
        qs=Employee.objects.get(id=id)
        
        return render(request,"emp_detail.html",{'employee':qs})


# @method_decorator(login_required(login_url='signin'), name='dispatch')
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
         id=kwargs.get('pk')
         Employee.objects.get(id=id).delete()
         messages.success(request,"Employee has been removed")
        #  redirect to emp_list (name mentioned in urls's path for ' listing the employees')
         return redirect("emp_list")



# @method_decorator(login_required(login_url='signin'), name='dispatch')
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Employee.objects.get(id=id)
        form=EmployeeForm(instance=obj)
        return render(request,"emp_edit.html",{"form":form})

    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Employee.objects.get(id=id)
        form=EmployeeForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            # Enployee.object.filter(id=id).update(**form.cleaned_data)
            
            messages.success(request,"Employee has been updated")
            return redirect("emp_list")
        else:
            messages.error(request,"Employee updation failed")
            return render(request,"emp_edit.html",{"form":form})

# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')    
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        # form=EmployeeForm(request.POST)
        # files=request.Files should be given if there is image
        form=RegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            
            MyUser.objects.create_user(**form.cleaned_data)
            # User.objects.create(**form.cleaned_data)
            messages.success(request,"Account has been created")
            return redirect("home")   
        else:
            messages.error(request,"Failed to create account")
            return render(request,"register.html",{"form":form})    


# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')    
class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            psd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=psd)
            if user is not None and not user.is_superuser:
                login(request, user)
                messages.success(request,"Login Success")
                form=LoginForm()  
                return redirect("userpage")
            elif user is not None and user.is_superuser:
                 messages.error(request,"Please Login as Admin")
                 return render(request,'login.html',{'form':form}) 
            
                  

            else:
                messages.error(request,"Invalid Credentials")
        form=LoginForm()       
        return render(request,'login.html',{'form':form}) 
            


# @method_decorator(login_required(login_url='signin'), name='dispatch')
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,"Logout Successfully")
        return redirect("signin")
    

# @method_decorator(login_required(login_url='signin'), name='dispatch')   
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class EmpHome(TemplateView):
    template_name="emphome.html"    

# class CourseCreateView(View):
#     def get(self,request,*args,**kwargs):
#         form=CourseForm()
#         return render(request,"course_add.html",{"form":form})

#     def post(self,request,*args,**kwargs):
#         form=CourseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Course Details has been added")
#             return redirect("home")   
#         else:
#             messages.error(request,"Failed to create Course")
#             return render(request,"home.html",{"form":form})    
    

# @method_decorator(login_required(login_url='signin'), name='dispatch')    
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class CourseCreateView(CreateView):
    model:Courses
    form_class=CourseForm
    template_name="course_add.html"
    success_url=reverse_lazy("home")

    # form-class
    # template-name   
        
# @method_decorator(login_required(login_url='signin'), name='dispatch')        
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class CourseListView(ListView):
    model=Courses
    template_name='course_list.html'
    context_object_name="courses"


# @method_decorator(login_required(login_url='signin'), name='dispatch')
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class UserListView(ListView):
    model=MyUser
    template_name='user_detail.html'
    context_object_name="user"

        # def get(self,request,*args,**kwargs):
        #     qs=Courses.objects.all()
        #     return render(request,"course_list.html",{"courses":qs})
    
    # modelname
    # template
    # context_key are the only changes

# class CourseDetailView(View):
#     def get(self,request,*args,**kwargs):
#         # kwargs={id:1}
#         # id=kwargs.get('id')
#         id=kwargs.get('pk')
#         qs=Courses.objects.get(id=id)
        
#         return render(request,"course_detail.html",{'courses':qs})
    
# @method_decorator(login_required(login_url='signin'), name='dispatch')    
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class CourseDetailView(DetailView):
   
    model=Courses
    template_name='course_detail.html'
    context_object_name="courses"


# @method_decorator(login_required(login_url='signin'), name='dispatch')
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class CourseEditView(UpdateView):
    model=Courses
    form_class=CourseForm
    template_name='course_edit.html'
    success_url=reverse_lazy("home")



# login_required(login_url='signin')
# cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
def course_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    Courses.objects.get(id=id).delete()
    return redirect("course_list")



# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class AdminLoginView(View):
    def get(self,request,*args,**kwargs):
        form=AdminLoginForm()
        return render(request,"admin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            psd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=psd)
            if user is not None and user.is_superuser:
                login(request, user)
                messages.success(request,"Login Success")
                return redirect("userdetail")
            else:
                messages.error(request,"You are Not An Admin")
                return render(request,'admin.html',{'form':form}) 


# @method_decorator(login_required(login_url='signin'), name='dispatch')
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class UserView(TemplateView):

    template_name="userpage.html"


# @method_decorator(login_required(login_url='signin'), name='dispatch')   
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class UserHome(TemplateView):
    template_name="userhome.html"      


# @method_decorator(login_required(login_url='signin'), name='dispatch')   
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class UserDetailView(DetailView):
    model=MyUser
    template_name='user_list.html'
    context_object_name="user"   



# @method_decorator(login_required(login_url='signin'), name='dispatch')   
# @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0), name='dispatch')
class UserEditView(UpdateView):
    model=MyUser
    form_class=RegistrationForm
    template_name='user_edit.html'
    success_url=reverse_lazy("userdetail")




# login_required(login_url='signin')
# cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
def user_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    User.objects.get(id=id).delete()
    return redirect("userdetail")

class BatchCreateView(CreateView,ListView):
    model=Batches
    form_class=BatchForm
    template_name="batch_add.html"
    context_object_name="batches"
    success_url=reverse_lazy("batch_add")

class BatchEditView(UpdateView):
    model=Batches
    form_class=BatchForm
    template_name="batch_edit.html"
    context_object_name="batches"
    success_url=reverse_lazy("batch_add")

class StudentCreateView(View):
    def get(self,request,*args,**kwargs):
        form1=UserProfileForm({"role":"student"})
        form2=StudentProfileForm()
        return render(request,"student_add.html",{"form1":form1,"form2":form2})

    def post(self,request,*args,**kwargs):
        # form=EmployeeForm(request.POST)
        # files=request.Files should be given if there is image
        form1=UserProfileForm(request.POST)
        form2=StudentProfileForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            usr=form1.save()
            form2.instance.user=usr
            form2.save()

            messages.success(request,"Student has been added")
            return redirect("home")   
        else:
            messages.error(request,"Student creation failed")
            return render(request,"student_add.html",{"form1":form1,"form2":form2})    


# creating student filter
from django_filters import FilterSet

class StudentFilter(FilterSet):

    class Meta:
        model = StudentProfile
        fields = ['batch', 'qualification']


class StudentListView(ListView):
    model=StudentProfile
    template_name='student_list.html'
    context_object_name="students"
    def get(self,request,*args,**kwargs):
        # f conatin both queryset and form now.
        f = StudentFilter(request.GET, queryset=StudentProfile.objects.all())
        return render(request, 'student_list.html', {'filter': f})
