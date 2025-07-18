from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.CharField(null=True)
  joined_date = models.DateField(null=True)
  gender = models.DateField(max_length=500, null = True)
  birthay = models.DateField(null=True)
  email = models.EmailField(max_length=255, null=True)

def __str__(self):
  return f"{self.firstname} {self.lastname}"