from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.conf import settings

from survey.models import Survey
from django.contrib.auth.models import User

# Create your views here.
def survey_overview(response):
    return HttpResponse(Survey.objects.all())


class create_survey(View):
    def get(self, request, id=None, *args, **kwargs):
        return render(request, "create_survey.html", {"form": SurveyForm()})

    def post(self, request, id=None, *args, **kwargs):
        Survey(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            creator=User.objects.get(pk=1),
        ).save()
        return redirect("/survey/")


class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ["title", "description"]
