from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
from .filters import fooditemFilter

@login_required(login_url='login')
@admin_only
# Create your views here.
def home():
    return

def userPage():
    return

def fooditem():
    return

def createfooditem():
    return

def registerPage():
    return

def loginPage():
    return

def logoutUser():
    return

def addFooditem():
    return