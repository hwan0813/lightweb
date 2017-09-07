from django.db import models

class Post(models.Model):
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    created_at2 = models.DateTimeField(auto_now_add=True)