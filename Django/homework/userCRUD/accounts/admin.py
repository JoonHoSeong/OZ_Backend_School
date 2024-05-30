from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomAdmin(UserAdmin):
    #만들 유저 모델을 사용
    # model = User
    list_display = ("username", "email", "phone_number", "created_at", "updated_at")
    filedsets = UserAdmin.fieldsets + (
        (None, {'fields' : ('phone_number',)})
    )
    