from ast import Delete
from base64 import encode
from cmath import log
from math import remainder
from multiprocessing import context
from operator import contains
from urllib import request
from urllib.request import Request
from webbrowser import get
from django import views
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render,redirect
import email
from email import message
from django.core.checks import messages
from pkg_resources import ResourceManager
import pkg_resources
from .models import *
from random import randint
from django.contrib.auth.models import User

# Create your views here.
def HomeView(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/home.html",{'all_job':all_job})
def IndexPage(request):
    return render(request,"app/index.html")

def SignupPage(request):
    return render(request,"app/signup.html")

def RegisterCandidate(request):
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = (request.POST['password'])
        #validation
        error_message = None
        if (not fname):
            error_message="firstname required"
        elif len(fname)<4:
            error_message="first name must be 4 char long"
        if (not lname):
            error_message="Lastname required"
        elif len(lname)<2:
            error_message="Lastname must be 2 char long"
        if (not email):
            error_message="Email required"
        elif len(lname)<4:
            error_message="Email must be 4 char long"
        if (not password):
            error_message="Password required"
        elif len(password)<8:
            error_message="Password must be 8 char long"



        #saving    
        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User Already Exists"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password:
                otp = randint(100000,999999)
                if not error_message:
                    newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                    newcandidate = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                    return render(request,"app/otpverify.html",{'email':email})
                else:
                    return render(request,"app/signup.html",{'error':error_message})
    else:
        if request.POST['role']=="Company":
            role = request.POST['role']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password =(request.POST['password'])
            #validation
            error_message = None
            if (not fname):
                error_message="firstname required"
            elif len(fname)<4:
                error_message="firstname must be 4 char long"
            if (not lname):
                error_message="Lastname required"
            elif len(lname)<2:
                error_message="Lastname must be 2 char long"
            if (not email):
                error_message="Email required"
            elif len(lname)<4:
                error_message="Email must be 4 char long"
            if (not password):
                error_message="Password required"
            elif len(password)<8:
                error_message="Password must be 8 char long"
            #saving  

            user = UserMaster.objects.filter(email=email)

            if user:
                message = "Company Already Exists"
                return render(request,"app/signup.html",{'msg':message})
            else:
                if password:
                    otp = randint(100000,999999)
                    if not error_message:
                        newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                        newcompany = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                        return render(request,"app/otpverify.html",{'email':email})
                    else:
                        return render(request,"app/signup.html",{'error':error_message})


def OtpPage(request):
    return render(request,"app/otpverify.html")

def Otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            message = "Otp Verify Successfully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "Otp is incorrect"
            return render(request,"app/otpverify.html",{'msg':message})
    else:
        message = "Registration Successfully"
        return render(request,"app/signup.html",{'msg':message})
    
def LoginPage(request):
    return render(request,"app/login.html")

def LoginUser(request):
    if request.POST['role']=="Candidate":
        email = request.POST['email']
        password = request.POST['password']
        user = UserMaster.objects.get(email=email)
        if user:
            #flag = check_password(password , user.password)
            if user.password==password and user.role=="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('index')
                
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "Email Invalid"
            return render(request,"app/login.html",{'msg':message})

    else:
        if request.POST['role']=="Company":
            email = request.POST['email']
            password =request.POST['password']
            user = UserMaster.objects.get(email=email)
            if user:
               # flag = check_password(password, user.password)
                if user.password==password and user.role=="Company":
                    company = Company.objects.get(user_id=user)
                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['firstname'] = company.firstname
                    request.session['lastname'] = company.lastname
                    request.session['email'] = user.email
                    request.session['password'] = user.password
                    return redirect('companyindex')
                else:
                    message = "Password does not match"
                    return render(request,"app/login.html",{'msg':message})
            else:
                message = "User does not exist"
                return render(request,"app/login.html",{'msg':message})


def CandidateLogout(request):
    return redirect('homepage')

def CompanyLogout(request):
    return redirect('homepage')
def AdminLogout(request):
    return redirect('homepage')

def ProfilePage(request,pk):
    user = UserMaster.objects.get(id=pk)
    can = Candidate.objects.get(user_id=user)
    return render(request,"app/profile.html",{'user':user,'can':can})


def UpdateProfile(request,pk):
    user = UserMaster.objects.get(id=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.contact = request.POST['contact']
        #validation
        error_message = None
        if (not can.contact):
            error_message="Contact required"
        elif len(can.contact)<10:
            error_message="contact must be 10 integer long"
        #saving
        can.state = request.POST['state']
        can.city = request.POST['city']
        can.gender = request.POST['gender']
        can.profile_pic = request.FILES['profilepic']
        can.experience = request.POST['experience']
        can.highestedu = request.POST['highestedu']
        can.job_type = request.POST['jobtype']
        can.jobcategory = request.POST['jobcategory']
        can.jobdescription = request.POST['jobdescription']
        can.shift = request.POST['shift']
        can.website = request.POST['website']
        can.max_salary = request.POST['maxsalary']
        can.min_salary = request.POST['minsalary'] 
        can.save()
        print("Data Saved")
        url = f"/profile/{pk}"
        return redirect(url,{'error':error_message})

def ApplyJobView(request,pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
        return render(request,"app/applyjob.html",{'user':user,'can':can,'job':job})


def ApplyJob(request,pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
        minsalary = request.POST['minsalary']
        maxsalary = request.POST['maxsalary']
        education = request.POST['highestedu']
        experience = request.POST['experience']
        website = request.POST['website']
        gender = request.POST['gender']
        logo = request.FILES['profilepic']

        applyjob = ApplyList.objects.create(candidate=can,job=job,min_salary=minsalary,max_salary=maxsalary,
                   highestedu=education,experience=experience,website=website,gender=gender,
                   resume=logo)
        
        msg = "Job Apply Succesfuully"
        return render(request,"app/index.html",{'msg':msg})




def CompanyIndexPage(request):
    return render(request,"app/company/index.html")

def CompanyProfilePage(request,pk):
    user = UserMaster.objects.get(id=pk)
    comp = Company.objects.get(user_id=user)
    return render(request,"app/company/profile.html",{'user':user,'comp':comp})

def UpdateCompanyProfile(request,pk):
    user = UserMaster.objects.get(id=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        comp.company_name = request.POST['company_name']
        comp.state = request.POST['state']
        comp.city = request.POST['city']
        comp.contact = request.POST['contact']
        comp.address = request.POST['address']
        comp.website = request.POST['website']
        comp.description = request.POST['description']
        comp.logo_pic = request.FILES['logo_pic']
        comp.save()
        print("Data Saved")
        url = f"/companyprofile/{pk}"
        return redirect(url)

def JobPostPage(request,pk):
    user = UserMaster.objects.get(id=pk)
    comp = Company.objects.get(user_id=user)
    return render(request,"app/company/jobpost.html",{'user':user,'comp':comp})

def JobDetailSubmit(request,pk):
    user = UserMaster.objects.get(id=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyaddress = request.POST['companyaddress']
        jobdescription = request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsibilities = request.POST['responsibilities']
        location = request.POST['location']
        salarypackage = request.POST['salarypackage']
        experience = request.POST['experience']
        website = request.POST['website']
        companyemail = request.POST['companyemail']
        companycontact = request.POST['companycontact']
        logo_pic = request.FILES['logo_pic']
        if (not companycontact):
            error_message="contact required"
        elif len(companycontact)<10:
            error_message="contact must be 10 integer long"
        if (not companyname):
            error_message="companyname required"
        elif len(companyname)<5:
            error_message="company must be 5 char long"

        newjob = JobDetails.objects.create(company_id=comp,jobname=jobname,companyname=companyname,companyaddress=companyaddress,
                    jobdescription=jobdescription,qualification=qualification,responsibilities=responsibilities,location=location,
                    companywebsite=website,companyemail=companyemail,companycontact=companycontact,salarypackage=salarypackage,
                    experience=experience,logo_pic=logo_pic)

        message = "Job Post Successfully"
        return render(request,"app/company/jobpost.html",{'msg':message})

def JobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/company/jobpostlist.html",{'all_job':all_job})


def CandidateJobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/job-list.html",{'all_job':all_job})


def ApplyJobList(request):
    all_jobapply = ApplyList.objects.all()
    return render(request,"app/company/applyjoblist.html",{'all_job':all_jobapply})
    
def AdminLoginView(request):
    return render(request,"app/admin/login.html")
def AdminIndexview(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request,"app/admin/inde.html")

def AdminLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    if username =="admin" and password =="root":
        request.session['username']=username
        request.session['password']=password
        return redirect('adminindex')
    else:
        message= "invalid password"
        HttpResponseNotFound(message)


def AdminUserList(request):
    all_user = UserMaster.objects.filter(role="Candidate")
    return render(request,"app/admin/userlist.html",{'alluser':all_user})
def AdminCompanyList(request):
    all_company = UserMaster.objects.filter(role="Company")
    return render(request,"app/admin/companylist.html",{'allcompany':all_company})

def UserDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('adminuserlist')

def CompanyDelete(request,pk):
    company = UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('admincompanylist')

def AdminVerifyCompany(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        return render(request,"app/admin/verify.html",{'company':company})
def AdminVerify(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified = request.POST['verify']
        company.save()
        return redirect('admincompanylist')

def Search(request):
    query = request.POST.get('query')
    job = JobDetails.objects.filter(jobname__icontains = query)

    context = {
        'job':job
    }
    return render(request,"app/search.html",context)

def JobDetailsPage(request):
    job = JobDetails.objects.all()
    return render(request,"app/job-details.html",{'job':job})



def AboutPage(request):
    return render(request,"app/about.html")

def ContactPage(request):
    if request.method=='POST':
        fname = request.POST['fullname']
        em = request.POST['email']
        sub = request.POST['subject']
        msg = request.POST['message']
        feed = Feedback(fullname=fname,email=em,subject=sub,message=msg)
        feed.save()
        return redirect('index')
    return render(request,"app/contact.html")
def AdminContactist(request):
    all_user = Feedback.objects.filter()
    return render(request,"app/admin/contactlist.html",{'alluser':all_user})

def linearsearch(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
arr = [JobDetails]
n = len(arr)
x= JobDetails
result = linearsearch(arr, n, x)
if(result == -1):
    print("not found")
else:
    print( result)