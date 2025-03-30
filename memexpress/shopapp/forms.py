from django import forms
from shopapp.models import Contacts

class FormComment(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)

    """
    rating = forms.ChoiceField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], label='Rating')"
    """

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['full_name', 'address', 'phone', 'email', 'active']  # Incluye todos los campos