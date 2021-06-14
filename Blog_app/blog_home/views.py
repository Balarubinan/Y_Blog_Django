import os

from django.shortcuts import render, redirect
from django.template import Template,loader
from django.http import HttpResponse
from .models import *

# Create your views here.
def show_blog_create(request):
    if request.method=="POST":
        print([x for x in request.POST])
        print(request.POST['text_editor'])
        title=request.POST['title']
        content=request.POST['text_editor']
        with open(f"{title}.html","w") as f:
            f.write(request.POST['text_editor'])
        return redirect("/blog/adminpage")
    template=loader.get_template("blog_home/blog_create.html")
    return HttpResponse(template.render({},request))

def show_dashboard(req):
    template = loader.get_template("blog_home/blog_dashboard.html")
    return HttpResponse(template.render({}, req))

def show_profile(req):
    template = loader.get_template("blog_home/admin_profile.html")
    return HttpResponse(template.render({}, req))

def show_login(req):
    context={}
    if req.method=="POST":
        email_gn=req.POST['email']
        password_gn=req.POST['password']
        if email==email_gn and password==password_gn:
            return redirect('/blog/adminpage')
        else:
            context={'error':"wrong"}
    template = loader.get_template("blog_home/admin_login.html")
    return HttpResponse(template.render(context, req))
