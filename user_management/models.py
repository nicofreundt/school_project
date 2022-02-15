from django.db.models import (
    CharField,
    BooleanField,
    ForeignKey,
    Model,
    CASCADE,
)
from django.core.validators import MinLengthValidator

### MODELS ####
class Creator(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name


class LoginID(Model):
    loginID = CharField(max_length=10, validators=[MinLengthValidator(4)])
    group = BooleanField()


class Participant(Model):
    loginID = ForeignKey(LoginID, default=0, on_delete=CASCADE)
