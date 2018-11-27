import unittest
from app.models import Location

class LocationTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the location class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_location = Location("Ngong View Apartments","Kilimani Rd","Kilimani","Milimani Estate")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

