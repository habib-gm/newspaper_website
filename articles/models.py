from django.contrib.auth import authenticate, get_user, get_user_model
from django.contrib.auth.models import User, UserManager
from django.db import models
from django.db.models import manager
from django.db.models.deletion import CASCADE
from django.db.models.manager import Manager
from django.urls import reverse

from users.models import CustomUser

class Article(models.Model):
    title = models.CharField(max_length= 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='authors',
        
        
    )
    seen = models.IntegerField( default = 1, null=False, blank= True )
    
    saw_users = models.ManyToManyField(
        get_user_model(),
        related_name='saw_by',
    )
    
    def __str__(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
    
    def latest(self, start = 0, finish = 5):
        return self.objects.latest('date')[start:finish]
    
    def incrementSeen(self, user:CustomUser):
        article = self
        print(User)
        self.user = user;
        Article.objects.filter(id= article.id).update(seen = article.seen +1 )
        if User.is_authenticated and User != article.author:
            Article.objects.get(pk = article.id).saw_users.add(CustomUser.objects.get(id = user.id))
           # Article.objects.get(id= article.id).save()
           
    def userPostCount(self):
        users = CustomUser.objects.all()
        user_list = []
        for user in users:
            articles = user.authors.all().only(name)
            user_list.append({user.id:articles.title})
        return user_list

class Comment(models.Model):
    
    article = models.ForeignKey(
        Article,
        on_delete = models.CASCADE,
        related_name='comments',
    )
    
    comment = models.CharField(max_length=140)
    
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('article_list')
        