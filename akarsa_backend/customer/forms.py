from django import forms
from . import models as customer_model




class Signupform(forms.ModelForm):
   
    class Meta:
        model=customer_model.Customer
        fields=["first_name","last_name","country_code","phone_number"]

class Otp_verify(forms.ModelForm):
        class Meta:
            model=customer_model.Customer
            fields=["otp"]
class Login(forms.ModelForm):
     class Meta:
            model=customer_model.Customer
            fields=["phone_number","country_code"]
class Dashboard(forms.ModelForm):
     class Meta:
            model=customer_model.Customer
            fields=["first_name","last_name","country_code","phone_number","gender","email","address_line_1","address_line_2","city","zip_code","state"]

class Payment(forms.Form):
    amount = forms.IntegerField()
    