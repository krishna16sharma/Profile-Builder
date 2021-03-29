from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
import csv
from . models import Students,State,Teachers,Teachers_data,Teachers_areas_of_interest
import pandas as pd
# Create your views here.

def index(request):
    if(Teachers_data.objects.count()==0):
        df1 = pd.read_csv('./table1.csv')
        nor1 = df1.shape[0]
        name_of_faculty = pd.Series(df1['name_of_faculty'])
        bio_of_faculty = pd.Series(df1['bio_of_faculty'])
        mail_of_faculty = pd.Series(df1['mail_of_faculty'])
        position = pd.Series(df1['position'])
        department = pd.Series(df1['department'])
        location = pd.Series(df1['location'])
        for i in range(nor1):
            teachers_data = Teachers_data(name_of_faculty=name_of_faculty[i],bio_of_faculty=bio_of_faculty[i],mail_of_faculty=mail_of_faculty[i],position=position[i],location=location[i],department=department[i])
            teachers_data.save()
    if(Teachers_areas_of_interest.objects.count()==0):
        df2 = pd.read_csv('./table2.csv')
        nor2 = df2.shape[0]
        name_of_faculty = pd.Series(df2['name_of_faculty'])
        faculty_research_interest = pd.Series(df2['Area of interest'])
        for i in range(nor2):
            teachers_areas_of_interest = Teachers_areas_of_interest(name_of_faculty=name_of_faculty[i],faculty_research_interest=faculty_research_interest[i])
            teachers_areas_of_interest.save()       
    return render(request,"index.html")

def login(request):
    print("Start!")
    if( request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        if (Students.objects.filter(mailid= email, password=password).exists() or Teachers.objects.filter(mailid= email, password=password).exists()):
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect("login")
    else:
        return render(request,"html/login.html")

def register(request):
    return render(request,"html/register.html")

def signup_students(request):
    if(request.method == 'POST'):
        img = request.POST['psimg']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        college = request.POST['col']
        degree = request.POST['deg']
        branch = request.POST['brh']
        semester = request.POST['sem']
        state = request.POST['stt']
        city = request.POST['sc']
        mailid = request.POST['mail_id']
        username = request.POST['username']
        password = request.POST['password']

        if Students.objects.filter(username=username).exists():
            messages.info(request,'Username Already Exists..Choose different Username')
            return redirect('signup_students')
        elif Students.objects.filter(mailid=mailid).exists():
            messages.info(request,'Mail id Already Exists..Choose different Mailid')
            return redirect('signup_students')
        else:
            student = Students(img=img,first_name = first_name,last_name = last_name,college = college,degree = degree,branch = branch,semester = semester,city = city,mailid = mailid,username = username,password = password)
            state = State(city=city,state=state)
            student.save()
            if (not State.objects.filter(city=city).exists()):
                state.save()
            messages.info(request,'Successfully registered! Login to continue.')
            return render(request,"index.html")
    else:
        return render(request,"html/signup_students.html")

def signup_teachers(request):
    if(request.method == 'POST'):
        img = request.POST['ptimg']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        college = request.POST['col']
        state = request.POST['stt']
        city = request.POST['sc']
        mailid = request.POST['mail_id']
        username = request.POST['username']
        password = request.POST['password']

        if Teachers.objects.filter(username=username).exists():
            messages.info(request,'Username Already Exists. Choose different Username')
            return redirect('signup_teachers')
        elif Teachers.objects.filter(mailid=mailid).exists():
            messages.info(request,'Mail id Already Exists. Choose different Mail id')
            return redirect('signup_teachers')
        else:
            teacher = Teachers(img=img,first_name = first_name,last_name = last_name,college = college,city = city,mailid = mailid,username = username,password = password)
            state = State(city=city,state=state)
            teacher.save()
            if (not State.objects.filter(city=city).exists()):
                state.save()
            messages.info(request,'Successfully registered! Login to continue.')
            return render(request,"index.html")
    else:
        return render(request,"html/signup_teachers.html")

def forgotpassword(request):
    return render(request,"html/forgotPassword.html")
