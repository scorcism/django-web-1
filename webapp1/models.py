from django.db import models

# Create your models here.
class filesUpload(models.Model):
    num_id = models.AutoField(primary_key=True)
    # ctime = models.DateTimeField()
    name = models.CharField(max_length=50, default="Not Provided")
    team = models.CharField(max_length=20, default="Not Provided")
    extra = models.CharField(max_length=300, default="Not Provided")
    topic = models.CharField(max_length=300, default="Not Provided")
    file = models.FileField()

    def __str__(self):
        return self.name +" Team:"+ self.team


    
class workFrom(models.Model):
    num_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    team = models.CharField(max_length=50, default="")
    ToWork = models.CharField(max_length=50, default="")
    Link = models.CharField(max_length=50, default="")
    lastDate = models.CharField(max_length=50, default="")
    extra = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name