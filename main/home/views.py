from django.shortcuts import render

# Create your views here.


#home_page view

def home_page(request):
    return render(request,'home.html')

def blog_template(request):
    return render(request,'blog_template.html')

def comment_section(request):
    return render(request,'comment_section.html')