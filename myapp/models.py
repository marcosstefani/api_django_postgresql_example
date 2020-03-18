from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=200, blank=False, unique=True, primary_key=True)
    birthday = models.DateField(blank=False)

    def __str__(self):
        return self.email
