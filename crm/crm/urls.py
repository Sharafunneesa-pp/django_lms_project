"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/add',views.EmployeeCreateView.as_view(),name="emp_add"),
    path('',views.IndexView.as_view(),name="home"),
    path('employee/all',views.EmployeeListView.as_view(),name="emp_list"),
    path('employee/<int:pk>',views.EmployeeDetailView.as_view(),name="emp_detail"),
    path('employee/remove/<int:pk>',views.EmployeeDeleteView.as_view(),name="emp_delete"),
    path('employee/change/<int:pk>',views.EmployeeEditView.as_view(),name="emp_edit"),
    path('employee/add',views.EmployeeCreateView.as_view(),name="emp_add"),
    path('register',views.RegistrationView.as_view(),name="register"),
    path('signin',views.SigninView.as_view(),name="signin"),
    path('signout',views.SignoutView.as_view(),name="signout"),
    path('emp/home',views.EmpHome.as_view(),name="emp_home"),
    path('courses/add',views.CourseCreateView.as_view(),name="course_add"),
    path('courses/all',views.CourseListView.as_view(),name="course_list"),
    path('courses/<int:pk>',views.CourseDetailView.as_view(),name="course_detail"),
    path('courses/change/<int:pk>',views.CourseEditView.as_view(),name="course_edit"),
    path('courses/remove/<int:pk>',views.course_delete_view,name="course_delete"),
    path('adminlogin',views.AdminLoginView.as_view(),name="adminlogin"),
    path('userpage',views.UserView.as_view(),name="userpage"),
    path('userdetail',views.UserListView.as_view(),name="userdetail"),
    path('userhome',views.UserHome.as_view(),name="userhome"),
    path('user/<int:pk>',views.UserDetailView.as_view(),name="user_list"),
    path('user/change/<int:pk>',views.UserEditView.as_view(),name="user_edit"),
    path('user/remove/<int:pk>',views.user_delete_view,name="user_delete"),
    path("batches/add",views.BatchCreateView.as_view(),name="batch_add"),
    path('batches/change/<int:pk>',views.BatchEditView.as_view(),name="batch_edit"),
    path('student/add',views.StudentCreateView.as_view(),name="student_add"),
    path('student/all',views.StudentListView.as_view(),name="student_all"),


    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
