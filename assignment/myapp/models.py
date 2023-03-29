from django.db import models

class Csv(models.Model):
    c1 = models.CharField(max_length=60)
    c2 = models.CharField(max_length=60)
    

    class Meta:
        ordering = ('id',)  
