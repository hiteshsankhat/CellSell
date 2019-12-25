from django import forms
from phone_field import PhoneField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=10)

    addressLine1 = forms.CharField(
        max_length=300,
        label='Address Line 1')
    # forms.Textarea(label="Address Line 1")
    addressLine2 = forms.CharField(
        max_length=300,
        label='Address Line 2', 
        required=False)
    city = forms.CharField(max_length=150)
    state = forms.CharField(max_length=150)
    pinCode = forms.CharField(max_length=10)    
    # phone = PhoneField(blank=True, help_text='Contact phone number')

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        addressLine1 = cleaned_data.get('addressLine1')
        addressLine2 = cleaned_data.get('addressLine2')
        city = cleaned_data.get('city')
        state = cleaned_data.get('state')
        pinCode = cleaned_data.get('pinCode')
        phone = cleaned_data.get('phone')


        if not phone.isnumeric():
            raise forms.ValidationError("Please enter valid number")


        