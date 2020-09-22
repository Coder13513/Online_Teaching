from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Assignment)
admin.site.register(Choice)
admin.site.register(Quiz)
admin.site.register(Question)