from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)

    type = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='post/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)