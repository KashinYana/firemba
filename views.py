# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from data.models import Data
from django.template import RequestContext

from forms import FormWithCaptcha

import json

def main(request):  
    
    captcha = FormWithCaptcha(request.POST)

    if request.method == 'POST' and captcha.is_valid():
        name = request.POST.get('inputName', '')
        surname = request.POST.get('inputSurName', '')
        patronymic = request.POST.get('inputPatronymic', '')
        phone = request.POST.get('inputPhone', '')
        email = request.POST.get('inputEmail', '')
        people = Data(name=name, surname=surname, patronymic=patronymic,phone=phone,email=email)
        people.save()
        
        response = render_to_response("landingpage.html", {'completed':'YES'}, context_instance=RequestContext(request))
        response.set_cookie('completed', 'YES')
        return response
    
    arg = {}
    if request.COOKIES.has_key('completed'):
        arg = {'completed':'YES'}
    else:
        arg = {'nocompleted': 'YES'}

    form = FormWithCaptcha()
    arg['form'] = form
    response = render_to_response("landingpage.html", arg, context_instance=RequestContext(request))
    return response
    
    
