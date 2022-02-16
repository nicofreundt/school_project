from django.db.models import (
    CharField,
    Model,
)
from django.forms import EmailField

### MODELS ####
class Creator(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = EmailField()
    # LDAP

    def __str__(self):
        return self.first_name + " " + self.last_name + " | " + self.email
