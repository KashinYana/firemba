# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from version.models import Version


import json
from django.views.decorators.csrf import csrf_exempt
import random

@csrf_exempt 
def main(request):
	
	response = None
	
	if not request.COOKIES.has_key('has_version'):
		version = random.randint(1, 6)
		response = render_to_response('landingpage-' + str(version)+ '.html')
		response.set_cookie('has_version', version)
		if len(Version.objects.filter(version = version)) == 0:
			newObject = Version(version = version, total = 1, success = 0)
			newObject.save()
		else:
			obj = Version.objects.get(version = version)
			obj.total += 1
			obj.save()
	else:
		version = request.COOKIES['has_version']	
		response = render_to_response('landingpage-' + str(version)+ '.html')
		
	if request.method == 'POST':
		name = request.POST.get('inputName', '')
		surname = request.POST.get('inputSurName', '')
		patronymic = request.POST.get('inputPatronymic', '')
		phone = request.POST.get('inputPhone', '')
		if request.COOKIES.has_key('has_version'):
			version = request.COOKIES['has_version']
			obj = Version.objects.get(version = version)
			obj.success += 1
			obj.save()
	return response
