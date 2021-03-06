import unittest
import os
from zencoder import Zencoder

class TestZencoder(unittest.TestCase):
    def setUp(self):
        """ Initialize Zencoder for testing """
        pass

    def test_api_key(self):
        """ initialize zencoder object and test api key """
        api_key = 'abcd123'
        zc = Zencoder(api_key=api_key)
        self.assertEquals(zc.api_key, api_key)

    def test_api_key_env_var(self):
        """ tests the ZENOCODER_API_KEY environment var """
        os.environ['ZENCODER_API_KEY'] = 'abcd123'
        zc = Zencoder()
        self.assertEquals(zc.api_key, 'abcd123')

if __name__ == "__main__":
    unittest.main()

