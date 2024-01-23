from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Enter your name"
        })
        self.fields['email'].widget.attrs.update({
            'class': "form-control",
            'placeholder': "Enter email address"
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Enter subject"
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Enter message",
            'rows': 9,
            'cols': 30
        })