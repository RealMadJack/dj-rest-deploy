from django.test import TestCase
from ..models import Puppy


class PuppyTest(TestCase):
    """Test module for Puppy module"""

    def setUp(self):
        Puppy.objects.create(name='Diana', age=1, breed='Pug', color='Apricot')
        Puppy.objects.create(name='Elizabeth', age=3, breed='Beagle', color='Orange Black')

    def test_puppy_breed(self):
        puppy_diana = Puppy.objects.get(name='Diana')
        puppy_beth = Puppy.objects.get(name='Elizabeth')
        self.assertEqual(puppy_diana.get_breed(), 'Diana belongs to Pug breed.')
        self.assertEqual(puppy_beth.get_breed(), 'Elizabeth belongs to Beagle breed.')
