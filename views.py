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
	setCompleted = False
			
	if request.method == 'POST':
		name = request.POST.get('inputName', '')
		surname = request.POST.get('inputSurName', '')
		patronymic = request.POST.get('inputPatronymic', '')
		phone = request.POST.get('inputPhone', '')
		email = request.POST.get('inputEmail', '')
		people = Data(name=name, surname=surname, patronymic=patronymic,phone=phone,email=email)
		people.save()
		setCompleted = True
		response.set_cookie('has_completed', 'YES')
	arg = {}
	if setCompleted or request.COOKIES.has_key('has_completed'):
		arg = {'completed':'YES'}
	else:
		arg = {'nocompleted': 'YES'}
	
	response = render_to_response("landingpage.html", arg)
	return response
