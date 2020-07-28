from django.db import models

class cell(models.Model):
    row_no = models.IntegerField()
    col_no = models.IntegerField()
    row_span = models.IntegerField()
    col_span = models.IntegerField()
    subject = models.CharField(max_length=200)