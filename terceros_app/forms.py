# terceros_app/forms.py
from django import forms
from .models import ThirdParty, Branch, City

class ThirdPartyForm(forms.ModelForm):
    class Meta:
        model = ThirdParty
        fields = [
            'business_name', 'third_party_type', 'location',
            'identification_type', 'identification_number', 'dv',
            'address', 'country', 'city'
        ]
        widgets = {
            'third_party_type': forms.Select(),
            'location': forms.Select(),
            'identification_type': forms.Select(),
            'country': forms.Select(),
            'city': forms.Select(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.country:
            self.fields['city'].queryset = self.instance.country.cities.order_by('name')

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = [
            'branch_number', 'main_address', 'delivery_address',
            'first_name_1', 'first_name_2', 'last_name_1', 'last_name_2',
            'position', 'mobile_phone', 'email'
        ]
        widgets = {
            'main_address': forms.TextInput(attrs={'placeholder': 'Por defecto, la dirección del tercero'}),
            'delivery_address': forms.TextInput(attrs={'placeholder': 'Por defecto, la dirección del tercero'}),
        }