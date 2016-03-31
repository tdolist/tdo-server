from django.db import models
from django.contrib.auth.models import User


class Tdo(models.Model):
    tdo_id = models.IntegerField()  # TODO make unique?
    name = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(
        'TdoUser',
        on_delete=models.CASCADE,
    )


class TdoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tokens = models.TextField(default="")

    @staticmethod
    def create(
        username,
        email,
        password,
        first_name,
        last_name
    ):
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_active = False
        user.save()

        return TdoUser.objects.create(user=user)

    def add_token(self, token):
        pass  # TODO method to add a new token

    def get_tokens(self):
        # return self.tokens.split()
        pass  # TODO method to get a list of tokens
