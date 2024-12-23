from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    REQUIRED_FIELDS=[]
    USERNAME_FIELD='email'
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('license_manager', 'License Manager'),
        ('tender_manager', 'Tender Manager'),
        ('internal_user', 'Internal User'),
    ]


    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(unique=True)
    password_str=models.CharField(max_length=255,null=True,blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    
    def __str__(self):
        return self.username

class AdditionalDetails(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
    state=models.CharField(max_length=50,null=True,blank=True)
    district=models.CharField(max_length=50,null=True,blank=True)
    pincode=models.CharField(max_length=10,null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.profile.first_name
    
class License(models.Model):
    LICENSE_TYPE = [
        ('manufacturing_license', 'Manufacturing License'),
        ('test_license', 'Test License'),
        ('import_license', 'Import License'),
        ('export_license', 'Export License'),
    ]

    application_type=models.CharField(max_length=50,choices=LICENSE_TYPE)
    application_number=models.CharField(max_length=50)
    license_number=models.CharField(max_length=50)
    date_of_submission=models.DateField()
    date_of_approval=models.DateField()
    expiry_date=models.DateField()

    PRODUCT_TYPE = [
        ('choice1', 'choice1'),
        ('choice2', 'choice2'),
        ('choice3', 'choice3'),
        ('choice4', 'choice4'),
    ]
    product_type=models.CharField(max_length=50,choices=PRODUCT_TYPE)
    product_name=models.CharField(max_length=100)
    model_number=models.CharField(max_length=50)
    intended_use=models.TextField(null=True,blank=True)
    CLASS_OF_DEVICE_TYPE = [
        ('choice1', 'choice1'),
        ('choice2', 'choice2'),
        ('choice3', 'choice3'),
        ('choice4', 'choice4'),
    ]
    class_of_device_type=models.CharField(max_length=50,choices=CLASS_OF_DEVICE_TYPE)
    software=models.BooleanField(default=False)
    legal_manufacturer=models.TextField(null=True,blank=True)
    agent_address=models.TextField(null=True,blank=True)
    accesories=models.TextField(null=True,blank=True)
    shell_life=models.TextField(null=True,blank=True)
    pack_size=models.IntegerField(default=0)
    attachments=models.FileField(null=True,blank=True)

    def __str__(self):
        return self.product_name




