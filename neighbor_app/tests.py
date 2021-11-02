from django.test import TestCase

from .models import Profile,NeighborHood,Business,Post
from django.contrib.auth.models import User

# Create your tests here.

class TestProfile(TestCase):
  def setUp(self):
    self.user = User(id=1, username='Lawrence', password='Lawize')
    self.user.save()

  def test_instance(self):
    self.assertTrue(isinstance(self.user, User))

  def test_save_user(self):
    self.user.save()

  def test_delete_user(self):
    self.user.delete()


class NeighborhoodTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='Lawrence')
    self.neighborhood = NeighborHood.objects.create(id=1, name='Ngomongo Village', description='One of villages in Korogocho Ward',image='https://myimages.com/image.png',created_at='2021,11,1',updated_at='2021,11,2', neighborhood=self.neighborhood,user=self.user,email='lawifirst@gmail.com')

  def test_create_neighborhood(self):
    self.neighborhood.create_neighborhood()
    neighborhood = NeighborHood.objects.all()
    self.assertTrue(len(neighborhood) > 0)

  def test_get_neighborhood(self, id):
    self.neighborhood.save()
    neighborhood = NeighborHood.get_neighborhood(neighborhood_id=id)
    self.assertTrue(len(neighborhood) == 1)


class BusinessTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='NgetichNIck')
    self.neighborhood = NeighborHood.objects.create(id=1, name='home')
    self.busines = Business.objects.create(id=1, name='Mama Mboga Business', description='Kukata na kuuza mboga and other vegetables',image='https://myimages.com/image.png',created_at='2021,11,1',updated_at='2021,11,2', neighborhood=self.neighborhood,user=self.user,email='lawifirst@gmail.com')

  def test_instance(self):
    self.assertTrue(isinstance(self.busines, Business))

  def test_create_business(self):
    self.busines.create_business()
    business = Business.objects.all()
    self.assertTrue(len(business) > 0)

  def test_get_business(self, id):
    self.business.save()
    business = Business.get_businesss(post_id=id)
    self.assertTrue(len(business) == 1)

