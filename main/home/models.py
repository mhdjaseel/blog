from django.db import models

# Create your models here.


class Comment(models.Model):
    person=models.TextField(max_length=10)
    comment_text=models.TextField(max_length=150)
    created_on=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.person

class post(models.Model):
    author=models.TextField(max_length=10)
    title=models.TextField(max_length=50)
    description=models.TextField(max_length=200)
    published_on=models.DateTimeField( auto_now_add=False)

    def __str__(self):
        return self.author