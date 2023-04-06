from django.db import models

# Create your models here.
class Table(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)


class Webpage(models.Model):
    topic_name=models.ForeignKey(Table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()


class AccessRecords(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()