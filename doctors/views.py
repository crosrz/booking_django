from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Doctors




def doctor_list(request):
	doctor_list= Doctors.objects.all()


	context= {'doctor_list' : doctor_list,}

	return render(request, 'Doctors/list.html', context)






def doctor_detail(request,slug):
	doctor_detail= Doctors.objects.get(slug=slug)

	context= {'doctor_detail' : doctor_detail,}


	return render(request, 'Doctors/detail.html',context )