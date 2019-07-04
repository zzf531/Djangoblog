from django.db import models


# 文章下面的评论
class Comment(models.Model):
    name = models.CharField(max_length=30)   # 名字
    text = models.TextField()  # 评论文本
    created_time = models.DateTimeField(auto_now_add=True) # 评论时间 auto_now_add 的作用是，当评论数据保存到数据库时，自动把 created_time 的值指定为当前时间
    post = models.ForeignKey('blog.Post', on_delete=True)

    def __str__(self):
        return self.text[:20]

