from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField

class Idea(models.Model):
    title : CharField = models.CharField(max_length=80)
    upvotes : IntegerField = models.IntegerField(default=0)
    description : CharField = models.CharField(max_length=1024)
    pub_date : DateField = models.DateField('date published')

    # TODO: add tags

