from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    carete_time = models.DateTimeField(auto_now_add=True)
    # auto_now_add 的作用是，当评论数据保存到数据库时，自动把 created_time 的值指定为当前时间

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

