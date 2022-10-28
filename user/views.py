import collections
import email
from django.shortcuts import HttpResponse, redirect, render
import requests
import json
import pymongo
from email import message
from typing import Collection
from pymongo import MongoClient



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

def index(request):
  try:
    request.session['email']
    return redirect('/home')
  except:
    return render(request,"index.html")

def login(request):
  try:
    request.session['email']
    return redirect('/home')
  except:
    return render(request,"login.html")

def logout(request):
  session_keys = list(request.session.keys())
  for key in session_keys:
    del request.session[key]
  return render(request,"index.html")


def goCreateAccount(request):
  return render(request,"signup.html")

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
  

#Login Via Email and Password
def loginVarification(request):
  if(request.method=='POST'):
    db = DBConnect.getInstance()
    collection = db["users"]
    email = request.POST['email']
    password = request.POST['password']

    if(collection.count_documents({"email":email ,"password":password})!=1):
      message = {"msg": "invalid email or password"}
      return render(request, 'html/login.html', message)     

    request.session['email'] = email
    
    return redirect("/home") 



#Create Account
def createAccount(request):
  if request.method =='POST':
    db = DBConnect.getInstance()
    collection = db['users']
    
    # taking information via POST method
    fName = request.POST['first_name']
    lName = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']

    msg = None
    
    
    if(collection.count_documents({"email": email})!=0):
      msg = "Email is already used"
      message = {"msg": msg}
      return render(request, 'signup.html', message)
    
    

    userInfo = {
        "name": fName+" "+lName,
        "email": email,
        "password": password,
        "gender": None,
        "phone_number": None,
        "bloodGroup": None,
        "homeAddress": None,
        "notification": [],
        "dp": "nodp.jpg",
        "cover":"noCover.jpeg"

    }

    request.session['email'] = email

    collection.insert_one(userInfo)
    return redirect("/home")


