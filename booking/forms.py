from django import forms

from .models import booking

class BookDoctorForm(forms.ModelForm):
	class Meta:
		model= booking
		fields= '__all__'


