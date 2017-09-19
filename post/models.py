from django.db import models

class Post(models.Model):
    
    title = models.CharField(max_length=100, help_text='여기에 제목을 입력!!')
    content = models.TextField(verbose_name="content",help_text='여기에 내용을 입력!!')
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    