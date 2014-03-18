# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from version.models import Version
from data.models import Data


import json
from django.views.decorators.csrf import csrf_exempt
import random

@csrf_exempt 
def main(request):
	
	responseName = ""
	setVersion = -1
	setCompleted = False
	
	if not request.COOKIES.has_key('has_version'):
		version = random.randint(1, 6)
		responseName = 'landingpage-' + str(version)+ '.html'
		setVersion = version
		if len(Version.objects.filter(version = version)) == 0:
			newObject = Version(version = version, total = 1, success = 0)
			newObject.save()
		else:
			obj = Version.objects.get(version = version)
			obj.total += 1
			obj.save()
	else:
		version = request.COOKIES['has_version']	
		responseName = 'landingpage-' + str(version)+ '.html'
		
	if request.method == 'POST':
		name = request.POST.get('inputName', '')
		surname = request.POST.get('inputSurName', '')
		patronymic = request.POST.get('inputPatronymic', '')
		phone = request.POST.get('inputPhone', '')
		email = request.POST.get('inputEmail', '')
		people = Data(name=name, surname=surname, patronymic=patronymic,phone=phone,email=email)
		people.save()
		if request.COOKIES.has_key('has_version'):
			version = request.COOKIES['has_version']
			obj = Version.objects.get(version = version)
			obj.success += 1
			obj.save()
		setCompleted = True
	arg = {}
	if setCompleted or request.COOKIES.has_key('has_completed'):
		arg = {'completed':'YES'}
	else:
		arg = {'nocompleted': 'YES'}
	print arg, version	
	response = render_to_response(responseName, arg)
	if setVersion != -1:
		response.set_cookie('has_version', setVersion)
	if setCompleted:
		response.set_cookie('has_completed', 'YES')
	return response
