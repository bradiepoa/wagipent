from django.db import models

# Create your models here.
from email.policy import default
from enum import unique
from pickle import FALSE
from pydoc import describe
from random import choices
from unicodedata import category
from django.db import models

# Create your models here.

class Location(models.Model):
    Company_name = models.CharField(max_length=200,unique=True, blank=True, null=True)
    P_o_box_no = models.CharField(max_length=200,unique=True, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.Company_name


class Email(models.Model):
    email= models.EmailField(unique=True, blank=True, null=True)
    describe_email = models.CharField(max_length=200,blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.email

class OfficePhone(models.Model):
    Phone_number= models.CharField(max_length=13, unique=True, blank=True, null=True)
    describe_Phone_number = models.CharField(max_length=200,blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.Phone_number


class sendUsMessage(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email= models.EmailField()
    subject = models.CharField(max_length=200)
    massege = models.TextField(max_length=200)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = (
        ('finished','finished'),
        ('progress','progress'),
    )
    name = models.CharField(max_length=200,unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to ='projects', blank=True,null=True)
    description = models.TextField()
    created_by = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200,choices=STATUS_CHOICES, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=False, auto_now=False)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class serviceCategory(models.Model):
    name = models.CharField(max_length=200,unique=True, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200,unique=True, blank=True, null=True)
    category = models.ForeignKey(serviceCategory, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to ='services', blank=True,null=True)
    description = models.TextField()
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=False, auto_now=False)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class background(models.Model):
    description = models.TextField(unique=True,)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.description
    

class goal(models.Model):
    description = models.TextField(unique=True,)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.description
    


class motor(models.Model):
    description = models.TextField(unique=True,)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.description


class mission(models.Model):
    description = models.TextField(unique=True,)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.description

class vission(models.Model):
    description = models.TextField(unique=True,)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.description


class mainObjective(models.Model):
    description = models.TextField(unique=True,)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.description


class StaffCaption(models.Model):
    description = models.TextField(unique=True,)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.description



class Staff(models.Model):
    Names = models.CharField(max_length=200, blank=True, null=True)
    tittle = models.CharField(max_length=200, blank=True, null=True)
    Phone = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200,blank=True, null=True)
    twitter = models.CharField(max_length=200,blank=True, null=True)
    faceBook = models.CharField(max_length=200,blank=True, null=True)
    instagram = models.CharField(max_length=200,blank=True, null=True)
    linkedin = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField(unique=True,)
    image = models.ImageField(upload_to ='team', blank=True,null=True)
    Date_joined = models.DateField(auto_now_add=False, auto_now=False)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.Names
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Parttener(models.Model):
    name = models.CharField(max_length=200,unique=True, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(unique=True,)
    Date_joined = models.DateField(auto_now_add=False, auto_now=False)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


class donationCaption(models.Model):
    description = models.TextField(unique=True,)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.description
