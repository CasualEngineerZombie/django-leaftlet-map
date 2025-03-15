from django import forms
from .models import UserLocation

class UserLocationForm(forms.ModelForm):
    class Meta:
        model = UserLocation
        fields = ['name', 'email', 'number', 'lat', 'lon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'email': forms.EmailInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'number': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'lat': forms.NumberInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2', 'step': 'any'}),
            'lon': forms.NumberInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2', 'step': 'any'}),
        }
