from django import forms
from django.forms import ModelForm
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import get_user_model

from .models import Question, Survey

# GLOBALS #
user_model = get_user_model()

# VIEWS #
def survey_overview(response):
    return render(
        response,
        "survey/overview.html",
        {"surveys": Survey.objects.all().order_by("title").iterator()},
    )


def survey_delete(request, survey):
    Survey.objects.get(id=survey).delete()
    return redirect("/survey/overview")


class survey_create(View):
    def get(self, request, id=None, *args, **kwargs):
        return render(request, "survey/create.html", {"surveyForm": SurveyForm()})

    def post(self, request, id=None, *args, **kwargs):
        if request.POST.get("closed") == "on":
            closed = True
        else:
            closed = False

        Survey(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            closed=closed,
            creator=user_model.objects.get(pk=1),
        ).save()
        return redirect("/survey/overview")


class survey_edit(View):
    def get(self, request, id=None, *args, **kwargs):
        survey = Survey.objects.get(pk=kwargs["survey"])
        surveyFormEdit = SurveyForm(
            {
                "title": survey.title,
                "description": survey.description,
                "closed": survey.closed,
            }
        )

        return render(
            request,
            "survey/edit.html",
            {
                "surveyForm": surveyFormEdit,
                "questions": survey.question_set.all().order_by('position'),
                "survey": survey.id,
            },
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


class question_create(View):
    def get(self, request, id=None, *args, **kwargs):
        return render(request, "question/create.html", {"questionForm": QuestionForm()})

    def post(self, request, id=None, *args, **kwargs):
        survey_id = request.path_info[13:49]
        Question(
            survey=Survey.objects.get(pk=survey_id),
            position=request.POST.get("position"),
            text=request.POST.get("text"),
        ).save()
        return redirect("/survey/edit/" + survey_id)


class question_edit(View):
    def get(self, request, id=None, *args, **kwargs):
        question = Question.objects.get(pk=kwargs["question"])
        questionFormEdit = QuestionForm(
            {
                "position": question.position,
                "text": question.text,
            }
        )

        return render(
            request,
            "question/edit.html",
            {"questionForm": questionFormEdit},
        )

    def post(self, request, id=None, *args, **kwargs):
        questionToEdit = Question.objects.get(pk=kwargs["question"])
        questionToEdit.title = request.POST.get("position")
        questionToEdit.description = request.POST.get("text")

        questionToEdit.save()

        return redirect("/survey/edit/" + questionToEdit.survey.id)


# MODEL-FORMS #
class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ["title", "description", "closed"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "margin: 0.5% 0px 1% 0px; padding: 0.5%",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "margin: 0.5% 0px 1% 0px; padding: 0.5%",
                }
            ),
            "closed": forms.CheckboxInput(
                attrs={
                    "class": "form-check form-check-input",
                    "style": "height: 4vh; width: 4vh; margin: 0.5% 0px 0.5% 0px",
                }
            ),
        }


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["position", "text"]
