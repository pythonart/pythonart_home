from django.db import models

# Create your models here.

from django.db import models

class MyProfile(models.Model):
    user=models.OneToOneField("auth.User")
    date_of_birth=models.DateField(null=True,help_text="2016-12-31 yyyy-mm-dd")
    mobile_number=models.CharField("Mobile Number",max_length=100,help_text="+CountryCode-PhoneNo")
    phone_number=models.CharField("Phone Number",max_length=100, help_text="+CountryCode-PhoneNo")
    company_name=models.CharField("Company name", max_length=100,help_text="Company Name")
    type_of_business=models.CharField("Business Or Institution Type",max_length=200,help_text="Logistics Company, School, Hospital")
    address=models.TextField("Company Address",null=True)

    
