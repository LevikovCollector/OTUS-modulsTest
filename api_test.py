import unittest
import requests
import random

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.domain = 'http://numbersapi.com/'
        self.numeric = random.randrange(0,100)
    def test_random_date(self):
       resp = requests.get(self.domain  + 'random/date')
       assert resp.headers.get('date') is not None
       assert resp.status_code == 200

    def test_info_about_num(self):
        resp = requests.get('{}{}'.format(self.domain, self.numeric))
        assert resp.text != ''
        assert resp.status_code == 200

    def test_math_fact(self):
        resp = requests.get('{}{}/math'.format(self.domain, self.numeric))
        assert resp.text != ''
        assert resp.status_code == 200


if __name__ == '__main__':
    unittest.main()
