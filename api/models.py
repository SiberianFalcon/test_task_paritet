from django.db import models


class Test_Task_Model(models.Model):
    text = models.TextField()
    picture = models.TextField()
