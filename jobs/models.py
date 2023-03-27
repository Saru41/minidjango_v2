from django.db import models

# Create your models here.


class Portal(models.Model):
    # TODO - refer
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id) + " portal - " + self.name
