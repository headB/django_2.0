from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=200)

class HeroInfo(models.Model):
    title = models.CharField(max_length=100)
    hbook = models.ForeignKey("BookInfo",on_delete='NULL')
