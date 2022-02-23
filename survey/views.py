from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.db.models.functions import Lower

from survey.models import Survey

# Create your views here.
def survey_overview(response):
    return render(
        response,
        "survey/overview.html",
        {"surveys": Survey.objects.all().order_by("title").iterator()},
    )


class create_survey(View):
    def get(self, request, id=None, *args, **kwargs):
        return render(request, "survey/create.html", {"form": SurveyForm()})

    def post(self, request, id=None, *args, **kwargs):
        Survey(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            creator=User.objects.get(pk=1),
        ).save()
        return redirect("/survey/overview")


class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ["title", "description"]
