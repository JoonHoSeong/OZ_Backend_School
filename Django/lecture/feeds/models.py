from django.db import models
from common.models import CommonModel
from django.conf import settings

# Create your models here.
class Feed(CommonModel):
    title = models.CharField(max_length=30)
    contents = models.CharField(max_length=200)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    