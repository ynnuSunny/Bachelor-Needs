from django.urls import path
from . import views
from part_time_job import views as ptjViews

urlpatterns =[
    path('job_home/',views.job_home,name = "job_home"),
    path('post_job/',views.postjob,name = "postjob"),
]
