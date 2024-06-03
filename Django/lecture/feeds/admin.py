from django.contrib import admin
from .models import Feed

# Register your models here.
@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    pass