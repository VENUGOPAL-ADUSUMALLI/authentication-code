from typing import Optional
from django.contrib.auth.hashers import make_password, check_password
from authentication.models import User


class UserStorage:


    def create_user(self, data: dict) -> User:

        user = User(
            email=data['email'],
            username=data['username'],
            phone_number=data['phone_number'],
            age=data['age'],
            gender=data['gender'],
            address=data['address'],
        )


        user.password = make_password(data['password'])


        if 'profile_picture' in data and data['profile_picture']:
            user.profile_picture = data['profile_picture']

        user.save()
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:

        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def get_user_by_username(self, username: str) -> Optional[User]:

        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def get_user_by_phone_number(self, phone_number: str) -> Optional[User]:

        try:
            return User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return None

    def check_credentials(self, email: str, raw_password: str) -> Optional[User]:

        user = self.get_user_by_email(email)
        if user and check_password(raw_password, user.password):
            return user
        return None
