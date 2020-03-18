from django.test import TestCase

from model_mommy import mommy
from django.utils.timezone import datetime
from datetime import datetime

from .models import User

class TestUser(TestCase):
      
  def setUp(self):
    self.user = mommy.make(
        User,
        first_name='Marcos',
        last_name='Rosa',
        email='marcos.cantor@gmail.com',
        birthday=datetime(1982,6,10).date
    )
      
  def test_user_creation(self):
      self.assertTrue(isinstance(self.user, User))
      self.assertEquals(self.user.__str__(), self.user.email)
