from django.db import models


# Create your models here.
class IdDefaultInfo(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    user_passwd = models.CharField(max_length=60)
    user_email = models.CharField(max_length=80)


class UserInfo(models.Model):
    user_favorite = models.CharField(max_length=90)
