import collections
import email
from django.shortcuts import HttpResponse, redirect, render
from django.core.files.storage import FileSystemStorage
import requests
import json
import pymongo
from email import message
from typing import Collection
from pymongo import MongoClient
from django.shortcuts import render
from django.db.models import Q
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
    db = DBConnect.getInstance()
    collection = db['jobcreateinfo']
    data = collection.find({})
    fs = FileSystemStorage()
    contest = {
         'data' : data
      }
    return render(request,"job_home.html",contest)


def post_job(request):
    return render(request,"post_job.html")


def createjob(request):
  if request.method =='POST':
    db = DBConnect.getInstance()
    collection = db['jobcreateinfo']
    # taking information via POST method

    email=request.session['email']
    job_title =request.POST['job_title']
    job_description= request.POST['job_description']
    salary = request.POST['salary']



    #saving information in database
    jobInfo = {
        "email" : email,
        "job_title": job_title,
        "job_description": job_description,
        "salary": salary,
    }
    collection.insert_one(jobInfo)
    return redirect("/job_home")

def Search_job(request):
    search_post = request.GET.get('search')
    db= DBConnect.getInstance()
    collection = db['jobcreateinfo']
    collection.find( { "job_title": {"$regex": search_post,"$options":'i'} }, { "job_description": {"$regex": search_post,"$options":'i'} }  )
    return render(request,"search_job_show.html")
