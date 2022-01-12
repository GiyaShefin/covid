from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from.models import PatientsDetails

class PatientForm(forms.ModelForm):
	class Meta:
		model = PatientsDetails
		fields = ['name', 'age','DOB', 'Address','district','Firstdose','SecondDose',]
# Create your forms here.