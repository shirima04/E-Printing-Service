from django.db import models

# Create your models here.
class PrintingService(models.Model):
    tasktype = models.CharField(max_length=50)#create a list to show 1.g w/k  2.ind w/k 3. repot 4.project 5.research
    slug = models.TextField()#guides to save your documents b4 uploading
    timeframe = models.DateTimeField()#set time frame for your task
    uploaddocument = models.FileField()#create a placeholder to show document format
    locationfordelivery = models.CharField(max_length=50)#enter ur location for delivery
    payment = models.IntegerField()#config for telephone payment
    status = models.CharField(max_length=50)#set status 1.printing on progress 2.wait for delivery 3.package delivered
    comment = models.TextField()#leave ur comment and suggestion
