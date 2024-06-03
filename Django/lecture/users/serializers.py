from rest_framework.serializers import ModelSerializer
from .models import User
# from feeds.serializers import 
from django.contrib.auth.validators import UnicodeUsernameValidator

class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_superuser')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }
        # depth = 1

class MyInfoUserSerializer(ModelSerializer) :
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {
        #     'username': {
        #         'validators': [UnicodeUsernameValidator()],
        #     }
        # }