from unicodedata import name
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.HomeView,name="homepage"),
    path("index",views.IndexPage,name="index"),
    path("signup/",views.SignupPage,name="signup"),
    path("register/",views.RegisterCandidate,name="register"),
    path("otppage/",views.OtpPage,name="otppage"),
    path("otp/",views.Otpverify,name="otp"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="loginuser"),
    path("profile/<int:pk>",views.ProfilePage,name="profile"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
    path("candidatejoblist/",views.CandidateJobListPage,name="candidatejoblist"),
    path("applyjob/<int:pk>",views.ApplyJobView,name="applyjob"),
    path("applyjoblist/<int:pk>",views.ApplyJob,name="applyjoblist"),
    path("candidatelogout/",views.CandidateLogout,name="canlogout"),




    path("companyindex/",views.CompanyIndexPage,name="companyindex"),
    path("companyprofile/<int:pk>/",views.CompanyProfilePage,name="companyprofile"),
    path("updatecompanyprofile/<int:pk>/",views.UpdateCompanyProfile,name="updatecompanyprofile"),
    path("jobpostpage/<int:pk>/",views.JobPostPage,name="jobpostpage"),
    path("jobdetails/<int:pk>/",views.JobDetailSubmit,name="jobdetails"),
    path("joblistpage/",views.JobListPage,name="joblistpage"),
    path("companylogout/",views.CompanyLogout,name="companylogout"),
    path("canapplyjoblist/",views.ApplyJobList,name="canapplyjoblist"),




    path("adminindex/",views.AdminLoginView,name="adminloginpage"),
    path("indexpage/",views.AdminIndexview,name="adminindex"),
    path("adminlogin/",views.AdminLogin,name="adminlogin"),
    path("adminuserlist/",views.AdminUserList,name="adminuserlist"),
    path("admincompanylist/",views.AdminCompanyList,name="admincompanylist"),
    path("adminuserdelete/<int:pk>",views.UserDelete,name="userdelete"),
    path('admincompanydelete/<int:pk>',views.CompanyDelete,name="admincompanydelete"),
    path("adminverify/<int:pk>",views.AdminVerifyCompany,name="adminverify"),
    path("adminverifypage/<int:pk>",views.AdminVerify,name="adminverifypage"),
    path("adminlogout/",views.AdminLogout,name="adminlogout"),

    path("search/",views.Search,name="search"),
    path("jobdetailspage/",views.JobDetailsPage,name="jobdetailpage"),
    path("aboutpage/",views.AboutPage,name="aboutpage"),
    path("contactpage/",views.ContactPage,name="contactpage"),
    path("adminfeedlist/",views.AdminContactist,name="adminfeedlist"),

]