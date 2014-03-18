from django.contrib import admin


# Register your models here.
from version.models import Version

admin.site.register(Version)
