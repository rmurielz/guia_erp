from django.db import models

# terceros_app/models.py
from django.db import models

class ThirdPartyType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class IdentificationType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    
    def __str__(self):
        return f"{self.name}, {self.country.name}"

class ThirdParty(models.Model):
    LOCATION_CHOICES = [
        ('Nacional', 'Nacional'),
        ('Exterior', 'Exterior'),
    ]
    
    business_name = models.CharField(max_length=200)
    third_party_type = models.ForeignKey(ThirdPartyType, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.SET_NULL, null=True)
    identification_number = models.CharField(max_length=50, unique=True)
    dv = models.CharField(max_length=5, blank=True, verbose_name="DV")
    address = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.business_name

class Branch(models.Model):
    third_party = models.ForeignKey(ThirdParty, on_delete=models.CASCADE, related_name='branches')
    branch_number = models.IntegerField()
    main_address = models.CharField(max_length=200)
    delivery_address = models.CharField(max_length=200)
    first_name_1 = models.CharField(max_length=100)
    first_name_2 = models.CharField(max_length=100, blank=True)
    last_name_1 = models.CharField(max_length=100)
    last_name_2 = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    def save(self, *args, **kwargs):
        if not self.main_address:
            self.main_address = self.third_party.address
        if not self.delivery_address:
            self.delivery_address = self.third_party.address
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.third_party.business_name} - Branch {self.branch_number}"