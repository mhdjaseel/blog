from django.urls import path
from .import views

urlpatterns = [
  
    path("", views.home_page, name="home_page"),
    path("blog_template/", views.blog_template, name="blog_template"),
    path("comment_section/", views.comment_section, name="comment_section"),

]


