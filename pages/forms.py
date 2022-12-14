from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length='50', required=True, widget=forms.TextInput(attrs={'class':'form-control', 'name': 'name', 'id': 'name'}))
    email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'name': 'email', 'id':'email'}))
    subject = forms.CharField(label='', max_length='500', required=True, widget=forms.TextInput(attrs={'class':'form-control', 'name': 'subject', 'id': 'subject'}))
    message = forms.CharField(label='', required=True, widget=forms.Textarea(attrs={'class':'form-control', 'name': 'message', 'id': 'message', 'placeholder': "Type your message here..."}))
