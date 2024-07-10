from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ResetPassword(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)