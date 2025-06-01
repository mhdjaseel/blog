from django.shortcuts import render
from .models import Comment,post
from django.utils.timezone import now
# Create your views here.


#home_page view

def home_page(request):
    blog=post.objects.all()
    return render(request,'home.html',{'data':blog ,'now':now()})

def blog_template(request):
    return render(request,'blog_template.html')

def comment_section(request):
    return render(request,'comment_section.html')