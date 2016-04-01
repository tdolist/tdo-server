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
    in_list = models.ForeignKey('TdoList', on_delete=models.CASCADE)

    '''
    @staticmethod
    def create(
            tdo_id,
            name,
            owner,
            add_to='default'):
        in_list = TdoList.objects.filter(owner=owner).get(name=add_to)
        return Tdo.objects.create(tdo_id, name, owner, in_list)
    '''


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
        tdo_user = TdoUser.objects.create(user=user)
        TdoList.objects.create(name='default', owner=tdo_user)  # TODO maybe move to registration function?
        return tdo_user

    def add_token(self, token):
        pass  # TODO method to add a new token

    def get_tokens(self):
        # return self.tokens.split()
        pass  # TODO method to get a list of tokens


class TdoList(models.Model):
    name = models.CharField(max_length=250)  # TODO should be unique
    owner = models.ForeignKey('TdoUser', on_delete=models.CASCADE)
