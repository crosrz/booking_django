from django.shortcuts import render
from .models import booking
from .forms import BookDoctorForm

# Create your views here.
from booking.models import booking


def book_doctor(request):

	book_form= BookDoctorForm()

	if request.method== 'POST' :
		book_form= BookDoctorForm(request.POST)


		if book_form.is_valid():
			book_form.save()




	context={'form': book_form}
	

	return render (request, 'booking/booking.html', context)
