import os

from django.shortcuts import render, redirect
from django.template import Template,loader
from django.http import HttpResponse
from .models import *
from datetime import datetime


# Create your views here.
def show_blog_create(request,name):
    if request.method=="POST":
        print([x for x in request.POST])
        print(request.POST['text_editor'])
        title=request.POST['title']
        content=request.POST['text_editor']
        with open(f"{title}.html","w") as f:
            f.write(content)

        new_blog=blog_table()
        new_blog.date=datetime.today()
        new_blog.blog_title=title
        new_blog.save()

        return redirect("/blog/adminpage")
    template=loader.get_template("blog_home/blog_create.html")

    if name!='new':
        file_content=''.join(open(name+".html",'r').readlines())
    else:
        file_content={}
    return HttpResponse(template.render({'file':file_content,'title':name},request))

def show_dashboard(req):
    blogs=blog_table.objects.all()
    template = loader.get_template("blog_home/blog_dashboard.html")
    return HttpResponse(template.render({'blogs':blogs}, req))

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
