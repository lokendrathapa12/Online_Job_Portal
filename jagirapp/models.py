from email import message
from django.db import models


# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)
        
    #@staticmethod
    #def get_user_by_email(email):
       # return UserMaster.objects.get(email=email)

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE,default="")
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    min_salary = models.CharField(max_length=250)
    max_salary = models.CharField(max_length=250)
    job_type = models.CharField(max_length=50,default="")
    jobcategory = models.CharField(max_length=50,default="")
    highestedu = models.CharField(max_length=50,default="")
    experience = models.CharField(max_length=50,default="")
    website = models.CharField(max_length=50,default="")
    shift = models.CharField(max_length=50,default="")
    jobdescription = models.CharField(max_length=100,default="")
    profile_pic = models.ImageField(upload_to="companyapp/img/candidate")

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE,default="")
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    state = models.CharField(max_length=50,default="")
    city = models.CharField(max_length=50,default="")
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150,default="")
    website = models.CharField(max_length=250,default="")
    description = models.CharField(max_length=500,default="")
    logo_pic = models.ImageField(upload_to="companyapp/img/company")

class JobDetails(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE,default="")
    jobname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    companyaddress = models.CharField(max_length=250)
    jobdescription = models.CharField(max_length=500)
    qualification = models.CharField(max_length=250)
    responsibilities = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    companywebsite = models.CharField(max_length=250)
    companyemail = models.CharField(max_length=250)
    companycontact = models.CharField(max_length=20)
    salarypackage = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)
    logo_pic = models.ImageField(upload_to="companyapp/img/company",default="")


class ApplyList(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE,default="")
    job = models.ForeignKey(JobDetails,on_delete=models.CASCADE,default="")
    min_salary = models.CharField(max_length=250)
    max_salary = models.CharField(max_length=250)
    highestedu = models.CharField(max_length=50)
    experience = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    gender = models.CharField(max_length=50)
    resume = models.ImageField(upload_to="app/resume",default="")


class Feedback(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=1000)


    
