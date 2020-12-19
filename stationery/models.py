from django.db import models
from multiselectfield import MultiSelectField


class Stationery(models.Model):    
    stationery_profile      = models.ImageField()
    stationery_name         = models.CharField(max_length = 100, unique = True)
    stationery_location     = models.CharField(max_length = 100)
    Stationery_slug         = models.TextField(max_length = 200)
    # Stationery_progress     = models.FilePathField() #This can cause an error when the path is not set then it fai to load when you run 
   
    # Stationery_service_offer
    Individual_Task         = models.BooleanField(default = True)
    Group_Task              = models.BooleanField(default = True) 
    Report                  = models.BooleanField(default = False)
    Research                = models.BooleanField(default = False)
    Paper                   = models.BooleanField(default = False)

    def __str__(self):
        return self.stationery_name

