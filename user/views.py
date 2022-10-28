from django.shortcuts import HttpResponse, render
import pymongo
from pymongo import MongoClient
from django.shortcuts import redirect, render


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
        db = cluster["users"]

        DBConnect.__instance = db
# Create your views here.

def index(request):
  return render(request,"index.html")

def login(request):
  return render(request,"login.html")
  
def goCreateAccount(request):
  return render(request,"signup.html")

def createAccount(request):
  if request.method =='POST':
    db = DBConnect.getInstance()
    collection = db['users']
    fName = request.POST['first_name']
    lName = request.POST['last_name']