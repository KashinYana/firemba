from django import forms
from fields import ReCaptchaField

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()
