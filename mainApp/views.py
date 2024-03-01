from django.shortcuts import render

def home(Request):
    return render(Request, "index.html")

def seccond(Request):
    return render(Request, "seccond.html")

def third(Request):
    return render(Request, "third.html")

def details(Request):
    return render(Request, "details.html")
