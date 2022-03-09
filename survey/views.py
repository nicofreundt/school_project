from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import get_user_model
from django.db.models.functions import Lower

from survey.models import Survey

user_model = get_user_model()

# VIEWS #
def survey_overview(response):
    return render(
        response,
        "survey/overview.html",
        {"surveys": Survey.objects.all().order_by("title").iterator()},
    )


class survey_create(View):
    def get(self, request, id=None, *args, **kwargs):
        return render(request, "survey/create.html", {"form": SurveyForm()})

    def post(self, request, id=None, *args, **kwargs):
        Survey(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            creator=user_model.objects.get(pk=1),
        ).save()
        return redirect("/survey/overview")


class survey_edit(View):
    def get(self, request, id=None, *args, **kwargs):
        s = Survey.objects.get(pk=kwargs["survey"])
        return render(request, "survey/edit.html", {"survey": s})


# MODEL-FORMS #
class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ["title", "description"]
