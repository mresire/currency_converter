from django.shortcuts import render
from currency_converter.forms import historyform
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from currency_converter.models import history
from datetime import datetime
# Create your views here.

def home(request):
	data = {}
	data['all'] = history.objects.all()
	return render(request, 'currency.html', data)

def savu(request):

	from_cy = request.POST.get('From')
	from_value = request.POST.get('From_value')
	to_cy = request.POST.get('To')
	to_value = request.POST.get('To_value')
	date = datetime.today()
	updater = history( From=from_cy, From_value=from_value, To=to_cy, To_value=to_value, Date=date)
	updater.save()
	return HttpResponseRedirect('home')
     

