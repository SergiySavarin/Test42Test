from django import forms
from .models import Owner


class EditContactForm(forms.ModelForm):
    """Form for edit contact information page."""
    class Meta:
        model = Owner
        # define common attribute class
        fc = 'form-control'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'name': 'first_name', 'id': 'first_name', 'class': fc}
            ),
            'last_name': forms.TextInput(
                attrs={'name': 'last_name', 'id': 'last_name', 'class': fc}
            ),
            'birthday': forms.DateInput(
                attrs={'name': 'birthday', 'id': 'birthday', 'class': fc}
            ),
            'email': forms.EmailInput(
                attrs={'name': 'email', 'id': 'email', 'class': fc}
            ),
            'skype': forms.TextInput(
                attrs={'name': 'skype', 'id': 'skype', 'class': fc}
            ),
            'jabber': forms.TextInput(
                attrs={'name': 'jabber', 'id': 'jabber', 'class': fc}
            ),
            'photo': forms.ClearableFileInput(
                attrs={'name': 'photo', 'id': 'photo', 'class': fc}
            ),
            'other_info': forms.Textarea(
                attrs={'name': 'other', 'id': 'other', 'class': fc}
            ),
            'bio': forms.Textarea(
                attrs={'name': 'bio', 'id': 'bio', 'class': fc}
            )
        }
