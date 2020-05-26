import unittest
import requests
import random
import requests_mock

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.domain = 'http://numbersapi.com/'
        self.numeric = random.randrange(0,100)

    @requests_mock.Mocker()
    def test_random_date(self, mock_req):
       mock_req.get(self.domain  + 'random/date', status_code=404)
       resp = requests.get(self.domain  + 'random/date')
       assert resp.status_code == 404

    @requests_mock.Mocker()
    def test_info_about_num(self, mock_req):
        mock_req.get('{}{}'.format(self.domain, self.numeric), status_code=500, text='mock_test')
        resp = requests.get('{}{}'.format(self.domain, self.numeric))

        assert resp.text == 'mock_test'
        assert resp.status_code == 500

    @requests_mock.Mocker()
    def test_math_fact(self, mock_req):
        mock_req.get('{}{}/math'.format(self.domain, self.numeric), status_code=200, text='mock_test')
        resp = requests.get('{}{}/math'.format(self.domain, self.numeric))
        assert resp.text == 'mock_test'
        assert resp.status_code == 200


if __name__ == '__main__':
    unittest.main()
