from django.shortcuts import  render, redirect



from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import  render
def detail_patient(request):
    return render(request,'vaccinationbooking.html')

	# details1 = PatientsDetails.objects.all()
	# # if request.method == 'POST':
	# 	name = request.POST.get('name', '')
	# 	dob = request.POST.get('date', '')
	# 	address=request.POST.get('address','')
	# 	district=request.POST.get('district','')
	# 	Firstdose=request.POST.get('Fisrtdose','')
	# 	Seconddose=request.POST.get('Seconddose','')
    #     patientdetails=Pa

def success_page(request):
    return render(request,'success.html')