from django import forms
from .models import Happy

class HappyForm(forms.ModelForm):
    class Meta:
        model = Happy
        fields = ['name', 'colour', 'power', 'image']
        
class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

