import collections
import email
from django.shortcuts import HttpResponse, redirect, render
import requests
import json
import pymongo
from email import message
from typing import Collection
from pymongo import MongoClient
import smtplib
import random



class DBConnect:
   __instance = None
   @staticmethod
   def getInstance():
      if DBConnect.__instance == None:
        DBConnect()
      return DBConnect.__instance
   def __init__(self):
      if DBConnect.__instance != None:
        raise Exception("This class is a singleton!")
      else:
        cluster = MongoClient("mongodb+srv://demo:demo@cluster0.csdz61e.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["bachelorNeeds"]

        DBConnect.__instance = db


def job_home(request):
    return render(request, "job_home.html")

def post_job(request):
    return render(request,"post_job.html")

def createjob(request):
  if request.method =='POST':
    db = DBConnect.getInstance()
    collection = db['jobcreateinfo']
    # taking information via POST method

    job_title =request.POST['job_title']
    job_description= request.POST['job_description']
    salary = request.POST['salary']
    job_poster = request.POST['job_poster']


    #saving information in database
    jobInfo = {
        "job_title": job_title,
        "job_description": job_description,
        "salary": salary,
        "job_poster": job_poster,
    }

    collection.insert_one(jobInfo)
    return redirect("/job_home")
