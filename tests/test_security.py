import unittest
import json
from app import app

class SecurityTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_security_headers(self):
        response = self.app.get('/')
        self.assertEqual(response.headers['X-Content-Type-Options'], 'nosniff')
        self.assertEqual(response.headers['X-Frame-Options'], 'SAMEORIGIN')
        self.assertEqual(response.headers['Referrer-Policy'], 'strict-origin-when-cross-origin')
        self.assertIn('Content-Security-Policy', response.headers)

    def test_calculate_non_dict_payload(self):
        # Sending a list instead of a dictionary at the root
        response = self.app.post('/calculate',
                                data=json.dumps([1, 2, 3]),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Invalid request: Payload must be JSON")

    def test_calculate_non_list_friends(self):
        response = self.app.post('/calculate',
                                data=json.dumps({"friends": "not a list"}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Invalid request: 'friends' must be a list")

    def test_calculate_player_limit(self):
        # 51 players
        friends = [[f"Player {i}", 0] for i in range(51)]
        response = self.app.post('/calculate',
                                data=json.dumps({"friends": friends}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Max 50 players allowed")

    def test_calculate_valid_request(self):
        # Ensure normal requests still work
        data = {
            "friends": [["Alice", 0], ["Bob", 0]],
            "buy_ins": {"Alice": 10, "Bob": 10},
            "chip_counts": {"Alice": {"red": 20}, "Bob": {"red": 0}},
            "chip_values": {"red": 0.5},
            "selected_chips": ["red"]
        }
        response = self.app.post('/calculate',
                                data=json.dumps(data),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('transactions', response.json)

if __name__ == '__main__':
    unittest.main()
