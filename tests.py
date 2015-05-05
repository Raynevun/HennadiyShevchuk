import unittest
from test_requests import RandomnessBeacon
import requests
URL = 'https://beacon.nist.gov/rest/record/last'
UNVALID_URL = 'https://beacon.nist.gov/rest/record'

class Test(unittest.TestCase):

    def test_valid_url(self):
        self.random_beacon = RandomnessBeacon(URL)
        self.assertEqual(self.random_beacon.r.status_code,200)

    def test_unvalid_url(self):
        self.random_beacon = RandomnessBeacon(UNVALID_URL)
        self.assertEqual(self.random_beacon.r.status_code, 404)

    def test_check_tag_output_value_with_unvalid_url(self):
        self.random_beacon = RandomnessBeacon(UNVALID_URL)
        self.random_beacon.get_output_value_tag()
        self.assertIsNone(self.random_beacon.tag_output_value)

    def test_check_tag_output_value_with_valid_url(self):
        self.random_beacon = RandomnessBeacon(URL)
        self.random_beacon.get_output_value_tag()
        self.assertIsNotNone(self.random_beacon.tag_output_value)
        self.assertEqual(type(self.random_beacon.tag_output_value),type(''))

    def test_call_get_result_function(self):
        self.random_beacon = RandomnessBeacon(URL)
        self.random_beacon.get_result()
        self.assertEqual(self.random_beacon.tag_output_value, None)

    def test_check_that_tag_output_value_is_not_null(self):
        self.random_beacon = RandomnessBeacon(URL)
        self.random_beacon.get_output_value_tag()
        self.assertTrue(len(self.random_beacon.tag_output_value))

    # def test_check_tag_output_content(self):
    #     self.random_beacon = RandomnessBeacon(URL)
    #     self.random_beacon.tag_output_value = '11111111111111111111111111111DFSS4'
    #     self.random_beacon.get_result()

if __name__ == "__main__":
    unittest.main()