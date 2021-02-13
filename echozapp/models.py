from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    writedate = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now) #장고에서 기본으로 제공됨
    # 들어갈 내용들 : 댓글 작성자, 댓글 내용, 댓글 작성 시간

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text

# Create your models here.
