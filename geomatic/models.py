from django.db import models
from django.http.request import MediaType
from django.contrib.auth.models import User
from Users.forms import User 

# Create your models here.

class LearniMaterials(models.Model):
    id=models.IntegerField(primary_key=True)
    YEAR=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    SEMESTER=(
        ('1','1'),
        ('2','2'),
    )
    Document_name=models.CharField(max_length=100)
    Course_name=models.CharField(max_length=100)
    Year=models.CharField(max_length=1,choices=YEAR)
    Semester=models.CharField(max_length=1,choices=SEMESTER)
    Document=models.FileField(upload_to='documents')
    date_added=models.DateField(auto_now_add=True) 
   
    class Meta:
        ordering=['-date_added']
        
    def level_1(self):
        return self.Year=='1'
        
    def level_2(self):
        return self.Year=='2'
            
    def level_3(self):
        return self.Year=='3'  
        
    def level_4(self):
        return self.Year=='4'           
        
    
        
class Video(models.Model):
    id=models.IntegerField(primary_key=True)
    author=models.CharField(max_length=50)
    vid_description=models.CharField(max_length=200)
    video_file=models.FileField(upload_to='videos')
    date_added=models.DateField(auto_now_add=True)
    
    
    
class Software(models.Model):
    id=models.IntegerField(primary_key=True)
    author=models.CharField(User,max_length=50)
    Software_description=models.CharField(max_length=200)
    Software_file=models.FileField(upload_to='softwares')
    date_added=models.DateField(auto_now_add=True)    
        