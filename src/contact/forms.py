from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
	name = forms.CharField(required = False )

	class Meta:
		model = Contact
		fields = ['name', 'email', 'comment']
