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





def main(request):
  try:
    request.session['email']
    return redirect('/home')
  except:
    return render(request,"main.html")

def index(request):
  try:
    request.session['email']
    return redirect('/home')
  except:
    return render(request,"index.html")

def login(request):
  if request.method == 'GET':
    try:
      request.session['email']
      return redirect('/home')
    except:
      return render(request,"login.html")
  if(request.method=='POST'):
    db = DBConnect.getInstance()
    collection = db["users"]
    email = request.POST['email']
    password = request.POST['password']

    if(collection.count_documents({"email":email ,"password":password})!=1):
      message = {"msg": "invalid email or password"}
      return render(request, 'login.html', message)     

    request.session['email'] = email
    
    return redirect("/home")

def signup(request):
  if request.method == 'GET':
    try:
      request.session['email']
      return redirect('/home')
    except:
      return render(request,"login.html")

  if request.method =='POST':
    db = DBConnect.getInstance()
    collection = db['users']
    
    # taking information via POST method
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']

    msg = None
    
    
    if(collection.count_documents({"email": email})!=0):
      msg = "Email is already used"
      message = {"msg": msg}
      return render(request, 'login.html', message)
    
    #for sending otp in user email
    otp = ""
    for i in range(6):
      n = random.randint(0,9)
      otp += str(n)
    
    sender_email = "bachelorneed@gmail.com"
    sender_pass = "csjcwenzefdejpwc"
    rec_email = email
    otp_msg  = "Your 6 digit otp is : "+otp
     
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,sender_pass)
    server.sendmail(sender_email,rec_email,otp)

    #saving user information in database
    userInfo = {
        "name": name,
        "email": email,
        "password": password,
        "gender": None,
        "phone_number": None,
        "bloodGroup": None,
        "homeAddress": None,
        "notification": [],
        "dp": "nodp.jpg",
        "cover":"noCover.jpeg",
        "otp": otp

    }

    request.session['email'] = email
    

    collection.insert_one(userInfo)
    return render(request, 'enterOtp.html')

def logout(request):
  session_keys = list(request.session.keys())
  for key in session_keys:
    del request.session[key]
  return render(request,"main.html")




def userVarification(request):
  if(request.method=='POST'):
    db = DBConnect.getInstance()
    collection = db["users"]
    email = request.session['email']
    otp = request.POST['otp']

    if(collection.count_documents({"email":email ,"otp":otp})!=1):
      message = {"msg": "invalid opt please try again with correct otp"}
      return render(request, 'enterOtp.html', message)     
    
    
    return redirect("/home") 


def home(request):
  try:
    request.session['email']
    return render(request,"home.html")
  except:
    return render(request,"index.html")


def profile(request):
  db = DBConnect.getInstance()
  collection = db['users']
  email = request.session['email']
  data = collection.find_one({"email":email})
  

