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
# Create your views here.



def goSpLogin(request):
  return render(request,"login2.html")

def goSpSingup(request):
  return render(request,"signup2.html")

def goOtp(request):
  return render(request,"enterOtp2.html")

#
def loginVarification2(request):
  if(request.method=='POST'):
    db = DBConnect.getInstance()
    collection = db["serviceProvider"]
    email = request.POST['email']
    password = request.POST['password']

    if(collection.count_documents({"email":email ,"password":password})!=1):
      message = {"msg": "invalid email or password"}
      return render(request, 'login.html', message)     

    request.session['email'] = email
    
    return redirect("/home") 


def checkOtp2(request):
  if(request.method=='POST'):
    db = DBConnect.getInstance()
    collection = db["serviceProviders"]
    nid = request.session['nid']
    otp = request.POST['otp']

    if(collection.count_documents({"nid":nid ,"otp":otp})!=1):
      message = {"msg": "invalid opt please try again with correct otp"}
      return render(request, 'enterOtp.html', message)     
    
    
    return render(request,"registration.html")

def signUp(request):
  if request.method =='POST':
    db = DBConnect.getInstance()
    collection = db['serviceProviders']
    
    # taking information via POST method
    name = request.POST['name']
    nid = request.POST['nid']
    phoneNumber = request.POST['phoneNumber']
    otp = "1234"
    msg = None
    
    
    if(collection.count_documents({"nid": nid})!=0 or collection.count_documents({"phoneNumber": phoneNumber})!=0):
      msg = "This nid or Phone number already Used"
      message = {"msg": msg}
      return render(request, 'signup.html', message)
    
    #for sending otp in user email
    

    #saving user information in database
    userInfo = {
        "name": name,
        "nid": nid,
        "phoneNumber": phoneNumber,
        "gender": None,
        "bloodGroup": None,
        "homeAddress": None,
        "notification": [],
        "dp": "nodp.jpg",
        "otp": otp,
    }

    request.session['nid'] = nid
    

    collection.insert_one(userInfo)
    return render(request,"enterOtp2.html") 