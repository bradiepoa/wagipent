from django.db import models
# Create your models here.
from email.policy import default
from enum import unique
from pickle import FALSE
from pydoc import describe
from random import choices
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
import uuid

# Create your models here.

# Create your models here.
class Banners(models.Model):
    CATE = (
		('home','home'),
		('about','about'),
		('team','team'),
        ('events','events'),
	)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categories = models.CharField(max_length=200, choices=CATE)
    Note = RichTextField()
    image = models.ImageField(upload_to='banners/')
    date = models.DateTimeField(auto_now_add=True,auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    class Meta:
        verbose_name_plural = '20. Banners'
    
    def __str__(self):
        return self.categories
    

    def clean(self):
        super().clean()
        if self.image.width < 1920 or self.image.height < 1088:
            raise ValidationError("Image minimum dimensions should be at least 1920x1088 pixels.")
        elif self.image.width > 1920 or self.image.height > 1088:
            raise ValidationError("Image  dimensions should be at most 1920x1088 pixels.")

class Location(models.Model):
    Company_name = models.CharField(max_length=200,unique=True)
    P_o_box_no = models.CharField(max_length=200,unique=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '03. Location'

    def __str__(self):
        return self.Company_name


class Email(models.Model):
    email= models.EmailField(unique=True)
    describe_email = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '02. Emails'


    def __str__(self):
        return self.email

class OfficePhone(models.Model):
    Phone_number= models.CharField(max_length=13, unique=True)
    describe_Phone_number = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '01. Office Phone'

    def __str__(self):
        return self.Phone_number


class sendUsMessage(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField()
    subject = models.CharField(max_length=200)
    massege = models.TextField(max_length=200)
    date_created = models.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name_plural = '19. sent Messages'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '18. Categories'
        
    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = (
        ('finished','finished'),
        ('progress','progress'),
    )
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to ='projects')
    description = RichTextField()
    created_by = models.CharField(max_length=200)
    status = models.CharField(max_length=200,choices=STATUS_CHOICES)
    is_published = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=False, auto_now=False)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '17. Project'

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def clean(self):
        super().clean()
        if self.image.width < 1920 or self.image.height < 1088:
            raise ValidationError("Image minimum dimensions should be at least 1920x1088 pixels.")
        elif self.image.width > 1920 or self.image.height > 1088:
            raise ValidationError("Image  dimensions should be at most 1920x1088 pixels.")


class serviceCategory(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '16. service Categories'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(serviceCategory, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to ='services')
    description = RichTextField()
    created_by = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=False, auto_now=False)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '15. Services'

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def clean(self):
        super().clean()
        if self.image.width < 1920 or self.image.height < 1088:
            raise ValidationError("Image minimum dimensions should be at least 1920x1088 pixels.")
        elif self.image.width > 1920 or self.image.height > 1088:
            raise ValidationError("Image  dimensions should be at most 1920x1088 pixels.")

class background(models.Model):
    description = RichTextField()
    created_by = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '14. Background'

    def __str__(self):
        return self.created_by
    

class goal(models.Model):
    description = RichTextField()
    created_by = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '13. Goal'

    def __str__(self):
        return self.description
    


class motto(models.Model):
    description = RichTextField()
    created_by = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '12. Motto'

    def __str__(self):
        return self.description


class mission(models.Model):
    description = RichTextField(unique=True,)
    created_by = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '11. mission'

    def __str__(self):
        return self.description

class vission(models.Model):
    description = RichTextField()
    created_by = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '10. vission'

    def __str__(self):
        return self.description


class mainObjective(models.Model):
    description = RichTextField()
    created_by = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '09. main objectives'

    def __str__(self):
        return self.description


class StaffCaption(models.Model):
    description = RichTextField()
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '08. staff Caption'

    def __str__(self):
        return self.description



class Staff(models.Model):
    Names = models.CharField(max_length=200)
    tittle = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,blank=True, null=True)
    twitter = models.CharField(max_length=200,blank=True, null=True)
    faceBook = models.CharField(max_length=200,blank=True, null=True)
    instagram = models.CharField(max_length=200,blank=True, null=True)
    linkedin = models.CharField(max_length=200,blank=True, null=True)
    description = RichTextField()
    image = models.ImageField(upload_to ='team')
    Date_joined = models.DateField(auto_now_add=False, auto_now=False)
    created_by = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '07. staff'

    def __str__(self):
        return self.Names
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def clean(self):
        super().clean()
        if self.image.width < 600 or self.image.height < 600:
            raise ValidationError("Image minimum dimensions should be at least 1920x1088 pixels.")
        elif self.image.width > 600 or self.image.height > 600:
            raise ValidationError("Image  dimensions should be at most 1920x1088 pixels.")


class Parttener(models.Model):
    name = models.CharField(max_length=200,unique=True, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField()
    Date_joined = models.DateField(auto_now_add=False, auto_now=False)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '06. Patterners'

    def __str__(self):
        return self.name


class contactDescription(models.Model):
    description = models.TextField(unique=True,)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '05. Contact Description'

    def __str__(self):
        return self.description


class Companies(models.Model):
    name  = models.CharField(max_length=200,unique=True, blank=True, null=True)
    image = models.ImageField(upload_to ='company', blank=True,null=True)
    our_link = models.URLField(max_length=200, blank=True,null=True)
    description  = RichTextField()
    is_published = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=False, auto_now=False)
    date_created = models.DateField(auto_now_add=True, auto_now=False)
    laste_update = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = '04. Companies'

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

    def clean(self):
        super().clean()
        if self.image.width < 600 or self.image.height < 600:
            raise ValidationError("Image minimum dimensions should be at least 1920x1088 pixels.")
        elif self.image.width > 600 or self.image.height > 600:
            raise ValidationError("Image  dimensions should be at most 1920x1088 pixels.")


class CurrentAndPreviousEvents(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=200)
    description = RichTextField()
    image       = models.ImageField(upload_to ='events')
    date        =  models.DateField(auto_now_add=True, auto_now=False)
    is_published = models.BooleanField(default=True)
    last_update  =  models.DateField(auto_now_add=False, auto_now=True)
    event_date   =  models.DateField(auto_now_add=False, auto_now=False)

    class Meta:
        verbose_name_plural = '21. Current And Previous Events'

    def __str__(self):
        return self.name

    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
