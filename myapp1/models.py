from typing import Iterable
from django.db import models
from PIL import Image

# Create your models here.
class Service(models.Model):
    icon=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)

    ordering=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.icon
    
   
    
class Testmonial(models.Model):
    image=models.ImageField(upload_to='testmonialImage/', blank=True, null=True)
    author=models.CharField(max_length=30)
    designation=models.CharField(max_length=50)
    description1=models.TextField(max_length=200)

    def __str__(self):
        return self.author

class Partner(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    logo=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title} "partnerPage"'
    
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=250)
    phone=models.CharField(max_length=12)
    message=models.TextField(max_length=300)

    def __str__(self):
        return self.name
    
class Contact_info(models.Model):
    title=models.CharField(max_length=30)
    email=models.EmailField(max_length=250)
    phone=models.CharField(max_length=12)
    mobile=models.CharField(max_length=12)
    web=models.URLField(max_length=50)

    def __str__(self):
        return f'{self.email} "ContactInfo"'
    
class Working_hour(models.Model):
    title=models.CharField(max_length=30)
    mon_wed=models.CharField(max_length=50)
    thus_fri=models.CharField(max_length=50)
    saturday=models.CharField(max_length=50)
    sunday=models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.title} "WorkingHourChanged"'
    

class Feature(models.Model):
    icon1=models.CharField(max_length=50)
    heading=models.CharField(max_length=50)
    description=models.CharField(max_length=200)

    ordering=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.heading
    
class Newfeature(models.Model):
    description=models.CharField(max_length=250)

    def __str__(self):
        return 'description'

    
class Portfolio(models.Model):
    image=models.ImageField(upload_to='portfolioImage/')
    title=models.CharField(max_length=40)
    link1=models.URLField(blank=True, null=True)
    link2=models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image)
        width, height = img.size
        target_width = 400
        #h_coefficient = width/600
        #target_height = height/h_coefficient
        target_height = 400
        img = img.resize((int(target_width), int(target_height)),Image.Resampling.LANCZOS)
        img.save(self.image.path, quality=100)
        img.close()
        self.image.close()

    def __str__(self):
        return self.title
    
class Banner(models.Model):
    image=models.ImageField(upload_to='bannerImage/')
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title
    
#model for Relation
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=50)
    addresss=models.CharField(max_length=50)
    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    teacher=models.ManyToManyField(Teacher)
    student_name=models.CharField(max_length=50)
    stu_number=models.IntegerField()
    def __str__(self):
        return self.student_name 
