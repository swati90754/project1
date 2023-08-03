from django.db import models

class Project(models.Model):

    pro_lang = [("Python","Python"),("Java","Java"),("PHP","PHP")]
    project_name = models.CharField(max_length=50)
    project_description = models.CharField(max_length=500)
    project_lead = models.CharField(max_length=50)
    programming_langauge = models.CharField(max_length=50,choices=pro_lang)
    project_start_date = models.DateTimeField()
    project_delivery_date = models.DateTimeField()