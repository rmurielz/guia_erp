from django.contrib import admin

# terceros_app/admin.py
from django.contrib import admin
from .models import ThirdPartyType, IdentificationType, Country, City, ThirdParty, Branch

@admin.register(ThirdPartyType)
class ThirdPartyTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(IdentificationType)
class IdentificationTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['country']

@admin.register(ThirdParty)
class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'identification_number', 'third_party_type']

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['third_party', 'branch_number', 'email']