import unittest
from app import app
import json

class SecurityTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_security_headers(self):
        response = self.app.get('/')
        self.assertIn('Content-Security-Policy', response.headers)
        self.assertEqual(response.headers.get('X-Content-Type-Options'), 'nosniff')
        self.assertEqual(response.headers.get('X-Frame-Options'), 'SAMEORIGIN')
        self.assertEqual(response.headers.get('Referrer-Policy'), 'strict-origin-when-cross-origin')

    def test_player_limit(self):
        friends = [["Player " + str(i), 0] for i in range(51)]
        response = self.app.post('/calculate',
                                 data=json.dumps({'friends': friends}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("limit", response.get_json().get('error', '').lower())

    def test_json_root_dict(self):
        response = self.app.post('/calculate',
                                 data=json.dumps([1, 2, 3]),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("must be a JSON object", response.get_json().get('error', ''))

if __name__ == '__main__':
    unittest.main()
