from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import CommonModel
# Create your models here.

class User(AbstractUser, CommonModel):
    #상속을 받아 생성, 수정 일자를 가지고 있음
    #핸드폰 번호를 추가하는 필드
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    def __str__(self) :
        return super().username