from django import forms
class NewRefcodeForm(forms.Form):
    # Add refcode Form
    ref_code = forms.CharField(max_length=35, required=True)
    system_number = forms.CharField(max_length=30,required=True)
    operation_number = forms.CharField(max_length=30,required=True)
    operation_name = forms.CharField(max_length=30, required=True)
    hmdescription = forms.CharField(max_length=300, required=True)
    fix_action = forms.CharField(max_length=300,required=True)
