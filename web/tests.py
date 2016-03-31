from django.test import TestCase
from web.models import *
from django.contrib.auth.models import User


class TdoUserTestCase(TestCase):
    def setUp(self):
        testuser = TdoUser.create(
            username='foobar',
            email='foo@bar.com',
            password='1234123412341324',
            first_name='Foo',
            last_name='Bar'
        )
        tdo1 = Tdo.objects.create(
            tdo_id=1,
            name='This is a test.',
            owner=testuser)
        tdo2 = Tdo.objects.create(
            tdo_id=2,
            name='This is another test.',
            owner=testuser)

    def test_user_creation(self):
        """Creating Users works as expected."""
        user1 = TdoUser.objects.get(user=User.objects.get(username='foobar'))
        self.assertEqual(user1.user.username, 'foobar')

    def test_tdo_addition(self):
        user1 = TdoUser.objects.get(user=User.objects.get(username='foobar'))
        tdo1 = Tdo.objects.get(tdo_id=1)
        self.assertEqual(tdo1.name, 'This is a test.')
