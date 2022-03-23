from django.contrib import admin
from .models import Survey, Question, Answer

# MODEL REGISTRATION #
admin.site.register([Survey, Question, Answer])
