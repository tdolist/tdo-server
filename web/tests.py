from django.test import TestCase
from web.models import *
from django.contrib.auth.models import User


class TdoDatabaseTestCase(TestCase):
    def setUp(self):
        """Set up the test environment by creating a new User."""
        TdoUser.create(
            username='foobar',
            email='foo@bar.com',
            password='1234123412341324',
            first_name='Foo',
            last_name='Bar'
        )

    def test_user_creation(self):
        """Creating Users works as expected."""
        user1 = TdoUser.objects.get(user=User.objects.get(username='foobar'))
        self.assertEqual(user1.user.username, 'foobar')
        self.assertEqual(len(TdoList.objects.filter(owner=user1)), 1,
                         "User 'foobar' should only have the 'default' list!")

    def test_list_creation(self):
        """New lists can be created."""
        user1 = TdoUser.objects.get(user=User.objects.get(username='foobar'))
        list1 = TdoList.objects.create(name='Cool new List',
                                       owner=user1)
        self.assertEqual(len(TdoList.objects.filter(owner=user1)), 2,
                         "User 'foobar' should have exactly 2 lists!")

    def test_tdo_addition(self):
        user1 = TdoUser.objects.get(user=User.objects.get(username='foobar'))
        def_list = TdoList.objects.get(owner=user1, name='default')
        new_list = TdoList.objects.create(name='Cool new List',
                                          owner=user1)
        tdo1 = Tdo.objects.create(
            tdo_id=1,
            name='This is a test.',
            owner=user1,
            in_list=def_list)
        tdo2 = Tdo.objects.create(
            tdo_id=2,
            name='This is another test.',
            owner=user1,
            in_list=new_list)
        tdo3 = Tdo.objects.create(
            tdo_id=3,
            name='Testing is essential.',
            owner=user1,
            in_list=new_list)
        self.assertEqual(len(Tdo.objects.filter(in_list=def_list)), 1,
                         "The 'default' list should contain exactly 1 entry!")
        self.assertEqual(len(Tdo.objects.filter(in_list=new_list)), 2,
                         "The 'Cool new List' should contain exactly 2 entries!")
