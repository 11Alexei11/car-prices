from django.contrib.auth.backends import BaseBackend

from .models import User


class EmailPasswordBackend(BaseBackend):
    @classmethod
    def authenticate(self, request, email=None, password=None):
        user = User.objects.filter(EMAIL=email, PASSWORD=password)
        if user.exists():
            return User.objects.get(EMAIL=email, PASSWORD=password)
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None