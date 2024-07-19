import os

from django.db import models


class TestTaskModel(models.Model):
    text = models.TextField()
    picture = models.ImageField(upload_to='images')

    def delete(self):
        os.remove(self.picture.path)
        super().delete()
