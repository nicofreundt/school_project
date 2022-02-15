from django.db.models import (
    CharField,
    IntegerField,
    BooleanField,
    ForeignKey,
    Model,
    CASCADE,
)
from user_management.models import LoginID, Creator

# Create your models here.
class Survey(Model):
    title = CharField(max_length=100)
    loginID = ForeignKey(LoginID, default="0000000000", on_delete=CASCADE)
    creator = ForeignKey(Creator, on_delete=CASCADE)
    closed = BooleanField()

    def __str__(self):
        return self.title


class Question(Model):
    survey = ForeignKey(Survey, on_delete=CASCADE)
    text = CharField(max_length=250)


class Answer(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    rating = IntegerField()
