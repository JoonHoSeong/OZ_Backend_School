from django.db import models

# Create your models here.
class CommonModel(models.Model):
    #통통으로 사용할 생성 수정 일을 생성
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #추상 클래스로 만들어서 상속받는 클래스에서 사용
    class Meta:
        abstract = True
