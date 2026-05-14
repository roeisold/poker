import unittest
from app import app
import json

class SecurityTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_calculate_no_json(self):
        resp = self.app.post("/calculate", data="not json", content_type='application/json')
        self.assertEqual(resp.status_code, 400)
        # Flask 2.3+ request.json is None if not JSON
        self.assertIn(b"Invalid request: Payload must be a JSON object", resp.data)

    def test_calculate_list_json(self):
        resp = self.app.post("/calculate", json=[1, 2, 3])
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Invalid request: Payload must be a JSON object", resp.data)

    def test_calculate_friends_not_list(self):
        resp = self.app.post("/calculate", json={"friends": "not a list"})
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Invalid request: 'friends' must be a list", resp.data)

    def test_calculate_large_friends(self):
        friends = [["Player " + str(i), 0] for i in range(51)]
        resp = self.app.post("/calculate", json={"friends": friends})
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Invalid request: Maximum 50 players allowed", resp.data)

    def test_security_headers(self):
        resp = self.app.get("/")
        self.assertEqual(resp.headers.get('X-Content-Type-Options'), 'nosniff')
        self.assertEqual(resp.headers.get('X-Frame-Options'), 'SAMEORIGIN')
        self.assertEqual(resp.headers.get('Referrer-Policy'), 'strict-origin-when-cross-origin')
        self.assertIn('Content-Security-Policy', resp.headers)

if __name__ == "__main__":
    unittest.main()
