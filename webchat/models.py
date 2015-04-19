from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name=models.CharField(max_length=200)
    create_time=models.DateTimeField(auto_now_add=True)


class User(models.Model):
    uid=models.CharField(max_length=200)
    uname=models.CharField(max_length=200)
    img=models.ImageField(max_length=200)
    password=models.CharField(max_length=200)
    scholar=models.CharField(max_length=200)
    feild=models.CharField(max_length=200)

class Article(models.Model):
    aid=models.CharField(max_length=200)
    uid=models.CharField(max_length=200)
    user=models.ForeignKey(User)
    tags=models.ManyToManyField(Tag,blank=True)
    atitle=models.CharField(max_length=200)
    subcomment=models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    mark=models.IntegerField()



class comment(models.Model):
    cid=models.CharField(max_length=200)
    article= models.ForeignKey(Article)
    content=models.CharField(max_length=1000)
    uid=models.CharField(max_length=200)




