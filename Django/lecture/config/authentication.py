from rest_framework.authentication import BaseAuthentication
import jwt
from django.conf import settings
from users.models import User

class JWTAuthentication(BaseAuthentication) :
    def authenticate(self, request):
        token = request.headers.get('jwt-auth')
        
        if not token :
            return None
        
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = decoded.get('id')
        user = User.objects.get(user_id=user_id)
        
        return (user, None)