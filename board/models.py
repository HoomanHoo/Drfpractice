from django.db import models


# Create your models here.
class Content(models.Model):
    user_id = models.ForeignKey(
        "member.IdDefaultInfo", on_delete=models.CASCADE, max_length=50
    )
    content_subject = models.CharField(max_length=100)
    content_article = models.TextField(max_length=3000)
