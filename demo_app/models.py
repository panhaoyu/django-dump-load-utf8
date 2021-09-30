from django.db import models


class DemoModel(models.Model):
    field = models.CharField(max_length=100)
