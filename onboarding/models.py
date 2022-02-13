from django.db.models import (
    CharField,
    IntegerField,
    BooleanField,
    ForeignKey,
    Model,
    CASCADE,
)
from django.core.validators import MinLengthValidator

# Create your models here.
class Creator(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name


class LoginID(Model):
    loginID = CharField(max_length=10, validators=[MinLengthValidator(4)])
    group = BooleanField()


class Survey(Model):
    title = CharField(max_length=100)
    loginID = ForeignKey(LoginID, default="0000000000", on_delete=CASCADE)
    creator = ForeignKey(Creator, on_delete=CASCADE)
    closed = BooleanField()

    def __str__(self):
        return self.title


class Participant(Model):
    loginID = ForeignKey(LoginID, default=0, on_delete=CASCADE)


class Question(Model):
    survey = ForeignKey(Survey, on_delete=CASCADE)
    text = CharField(max_length=250)


class Answer(Model):
    quaetion = ForeignKey(Question, on_delete=CASCADE)
    rating = IntegerField()
