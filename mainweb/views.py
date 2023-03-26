from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . forms import ContactForm
from . models import (sendUsMessage,Location,Email,OfficePhone,Project,Category,Service,background,goal,motor,mission,vission,
mainObjective,StaffCaption,Staff,Parttener,contactDescription,Companies
)

from django.contrib import messages

# Create your views here.

def Home_view(request):
	services = Companies.objects.order_by('-date_created').filter(is_published=True)
	back = background.objects.order_by('-date_created').filter(is_published=True)
	goals = goal.objects.order_by('-date_created').filter(is_published=True)
	mot = motor.objects.order_by('-date_created').filter(is_published=True)
	querryset = Service.objects.order_by('-date').filter(is_published=True)

	misso = mission.objects.order_by('-date_created').filter(is_published=True)
	visso = vission.objects.order_by('-date_created').filter(is_published=True)
	mbj = mainObjective.objects.order_by('-date_created').filter(is_published=True)
	dona = contactDescription.objects.order_by('-date_created').filter(is_published=True)

	patt = Parttener.objects.order_by('-date_created').filter(is_published=True)

	context = {'services':services}
	context = {
		'back':back, 'goals':goals,'mot':mot, 'misso':misso
		, 'visso':visso,'mbj':mbj,'services':services,"dona":dona,"patt":patt,'querryset':querryset
		}
	return render(request, 'mainweb/index.html',context)


def About_view(request):
	back = background.objects.order_by('-date_created').filter(is_published=True)
	goals = goal.objects.order_by('-date_created').filter(is_published=True)
	mot = motor.objects.order_by('-date_created').filter(is_published=True)

	misso = mission.objects.order_by('-date_created').filter(is_published=True)
	visso = vission.objects.order_by('-date_created').filter(is_published=True)
	mbj = mainObjective.objects.order_by('-date_created').filter(is_published=True)

	capt = StaffCaption.objects.order_by('-date_created').filter(is_published=True)

	team = Staff.objects.order_by('-date_created').filter(is_published=True)

	patt = Parttener.objects.order_by('-date_created').filter(is_published=True)
	querryset = Service.objects.order_by('-date').filter(is_published=True)
	

	context = {
		'back':back, 'goals':goals,'mot':mot, 'capt':capt,'misso':misso
		, 'visso':visso,'mbj':mbj,'capt':capt,'team':team,'patt':patt,'querryset':querryset
		}
	return render(request, 'mainweb/about.html',context)

def Services_view(request):
	querryset = Service.objects.order_by('-date').filter(is_published=True)
	projects = Project.objects.order_by('-date').filter(status='finished')

	context = {'querryset':querryset,"projects":projects,'querryset':querryset}
	return render(request, 'mainweb/services.html',context)

def serviceDetail(request,pk):

	services = Service.objects.get(id=pk)
	serv = Service.objects.order_by('-date').filter(is_published=True)
	querryset = Service.objects.order_by('-date').filter(is_published=True)

	context = {'services':services, 'serv':serv,'querryset':querryset}
	return render(request, 'mainweb/service.html',context)

def Projects_view(request):
	category = request.GET.get('category')

	if category == None:

		projects = Project.objects.order_by('-date').filter(is_published=True)
	else:
		projects = Project.objects.filter(category__name=category)
	
	# pagination
	paginator =Paginator(projects,1)
	page = request.GET.get('page')

	try:
		proj = paginator.page(page)
	except PageNotAnInteger:
		proj = paginator.page(1)
	except EmptyPage:
		proj = paginator.page(paginator.num_pages)

	categories = Category.objects.all()
	querryset = Service.objects.order_by('-date').filter(is_published=True)

	context = {'projects':projects, 'categories':categories, 'page':page,"proj":proj,'querryset':querryset}
	return render(request, 'mainweb/projects.html', context)

def Projectview(request,pk):
	projects = Project.objects.get(id=pk)
	project = Project.objects.order_by('-date').filter(is_published=True)
	querryset = Service.objects.order_by('-date').filter(is_published=True)

	context = {'projects':projects, 'project':project,'querryset':querryset}
	return render(request, 'mainweb/project.html', context)


def Team_view(request):
	team = Staff.objects.order_by('-date_created').filter(is_published=True)
	querryset = Service.objects.order_by('-date').filter(is_published=True)

	context = {'team':team,'querryset':querryset}
	return render(request, 'mainweb/team.html', context)

def singleTeam(request, pk):	
	team = Staff.objects.get(id=pk)
	querryset = Service.objects.order_by('-date').filter(is_published=True)
	context = {'team':team,'querryset':querryset}
	return render(request ,'mainweb/single_team.html',context)


def Contacts_view(request):
	querryset = Service.objects.order_by('-date').filter(is_published=True)
	locate = Location.objects.all().order_by('-date_created')
	emailz = Email.objects.all().order_by('-date_created')
	phones = OfficePhone.objects.all().order_by('-date_created')
	form = ContactForm()
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Your message recieved succefully, Team shall get to you in a shotest time possible")
			return redirect('mainweb:contactus')
	context = {'form':form,'locate':locate,'emailz':emailz,'phones':phones,'querryset':querryset}
	return render(request, 'mainweb/contacts.html', context)
