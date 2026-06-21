from django.db import models
from datetime import datetime
from django.core.validators import MaxLengthValidator,MaxValueValidator,MinValueValidator,MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200)
    age =models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
   
"""field type , option field ,extranal field , relationship
pip install django-multiselectfield
pip install django-phonenumber-field phonenumbers
""" 
GENDER_FIELD =( 
    ('male','male'),
    ('female','female'),
    ('other','other')
)
SUBJECT_FIELD =(
    ('django','django'),
    ('python','python')
)
class Contact(models.Model):
    iswork = models.BooleanField(default=True,verbose_name="click here if it works")
    name = models.CharField(max_length=200,default="sujan",validators=[MinLengthValidator(4)])
    message = models.TextField(blank=True)
    # 32 bits sign --> -2^32 --> 2^32   
    age = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(100)])
    stock = models.BigIntegerField()
    stock_1 = models.SmallIntegerField()
    stock_1 = models.PositiveSmallIntegerField()
    email = models.EmailField(null=True, unique=True)
    image = models.ImageField(upload_to="images")
    file = models.FileField(upload_to="files")
    dob = models.DateField(default=datetime.now())
    date_field = models.DateTimeField(default=datetime.now())
    creat_at = models.DateField(auto_now_add=True,null=True)
    update_at = models.DateField(auto_now=True,null=True) #update 
    gender = models.CharField(max_length=20,choices=GENDER_FIELD,null=True)
    subject = MultiSelectField(choices=SUBJECT_FIELD,null=True)
    phone = PhoneNumberField(blank=True,region='NP')
    
class Signup(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)
    
    
    