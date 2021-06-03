from django.shortcuts import render
from django.template import Template,loader
from django.http import HttpResponse

# Create your views here.
def blog_preview(request):
    template=loader.get_template("blog_home/blog_create.html")
    return HttpResponse(template.render({},request))

