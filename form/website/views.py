from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req, "home.html") 
def save_student(req):
    name = req.POST.get("student_name")
    student_mobile = req.POST.get("student_mobile")
    student_email = req.POST.get("student_email")
    student_city = req.POST.get("student_city")
    print(name)
    print(student_mobile)
    print(student_email)
    print(student_city)
    return redirect("/")