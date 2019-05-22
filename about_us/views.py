from django.shortcuts import render
from .models import AboutUs, Members

# Create your views here.
def about_us_list(request):
	aboutus= AboutUs.objects.last()
	members=Members.objects.all()


	context={

	'aboutus' : aboutus,
	'members' : members,

	}

	return render(request, 'about_us/aboutus.html', context)
