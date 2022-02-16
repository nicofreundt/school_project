from re import A
from django.contrib import admin
from .models import Creator
from survey.models import Survey, Question, Answer

# Register your models here.
admin.site.register(Creator)
admin.site.register([Survey, Question, Answer])
