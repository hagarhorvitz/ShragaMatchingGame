from django.db.models import Model, CharField, DecimalField, IntegerField, ForeignKey, RESTRICT, DateField
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator

# Create your models here.

class AnimalModel():

    name = CharField(max_length=40, required = True, validators=[MinLengthValidator(2), MaxLengthValidator(50)])

    class Meta:
        db_table = "animals"