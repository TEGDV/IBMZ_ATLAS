# Forms ♥

# Django
from django import forms
class EmployeeProfileUpdateForm(forms.Form):
    # Profile Form
    picture = forms.ImageField(required=False)
    website = forms.URLField(max_length=200, required=False )
    biography = forms.CharField(max_length=200,required=True)
    resume = forms.FileField(required=False)
    phone_number = forms.CharField(max_length=50,required=False)
    position = forms.CharField(max_length=50, required=False)
    shift = forms.CharField(max_length=25, required=False)
