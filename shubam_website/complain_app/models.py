from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Complain(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    room = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now=True)
    complain_noted = models.BooleanField(default=False)
    complain_complete = models.BooleanField(default=False)
    rollno= models.CharField(max_length=200,null=True)
    student_email = models.EmailField(null=True)



    def get_absolute_url(self):
        #return reverse("post_detail",kwargs={'pk':self.pk})
        return reverse('complain_list')


    def __str__(self):
        return self.title
