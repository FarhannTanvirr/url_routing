from django.db import models

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date  = models.DateTimeField('date published')
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
class collection(models.Model):
    title = models.CharField(max_length=200)
class product(models.Model):
    title = models.CharField(max_length=200)
    description  = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.ImageField()
    last_update  =models.DateTimeField(auto_now=True)
    collection =models.ForeignKey(collection,on_delete=models.PROTECT)
    
    
class User(models.Model):
    name = models.CharField(max_length=200)
    