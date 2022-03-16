from django.forms import ModelForm
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import get_user_model

from survey.models import Survey

# GLOBALS #
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
        return render(request, "survey/create.html", {"surveyForm": SurveyFormCreate()})

    def post(self, request, id=None, *args, **kwargs):
        Survey(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            creator=user_model.objects.get(pk=1),
        ).save()
        return redirect("/survey/overview")


class survey_edit(View):
    def get(self, request, id=None, *args, **kwargs):
        survey = Survey.objects.get(pk=kwargs["survey"])
        surveyFormEdit = SurveyFormEdit(
            {
                "title": survey.title,
                "description": survey.description,
                "closed": survey.closed,
            }
        )

        return render(
            request,
            "survey/edit.html",
            {"surveyForm": surveyFormEdit, "survey": survey},
        )

    def post(self, request, id=None, *args, **kwargs):
        if request.POST.get("closed") == "on":
            closed = True
        else:
            closed = False

        surveyToEdit = Survey.objects.get(pk=kwargs["survey"])
        surveyToEdit.title = request.POST.get("title")
        surveyToEdit.description = request.POST.get("description")
        surveyToEdit.closed = closed

        surveyToEdit.save()

        return redirect("/survey/overview")


# MODEL-FORMS #
class SurveyFormCreate(ModelForm):
    class Meta:
        model = Survey
        fields = ["title", "description"]


class SurveyFormEdit(ModelForm):
    class Meta:
        model = Survey
        fields = ["title", "description", "closed"]
