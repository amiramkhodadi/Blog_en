from django import forms
class ContactUsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=1)
    text = forms.CharField(max_length=1, label='Your Message')