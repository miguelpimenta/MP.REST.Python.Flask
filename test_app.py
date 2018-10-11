import unittest
from app import app
from app import router as r
from flask import jsonify

class TestAPILocally(unittest.TestCase):

    def setUp(self):
        self.client = app.app_context()
        self.client.push()

    def tearDown(self):
        self.client.pop()

    def test_create_user(self):
        with app.app_context():
            retVal = r.create_user()
            #if isinstance(retVal, list):
            #   res = jsonify([str(v) for v in retVal]), 201
            self.assertTrue(retVal[1] == 501 or retVal[1] == 200)

    def test_read_user(self):
        with app.app_context():
            retVal = r.read_user(1)
            self.assertTrue(retVal[1] == 501 or retVal[1] == 200)

    def test_update_user(self):
        with app.app_context():
            retVal = r.update_user(1)
            self.assertTrue(retVal[1] == 501 or retVal[1] == 200)

if __name__ == '__main__':
    unittest.main()