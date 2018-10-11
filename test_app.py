import unittest
from app import app
from app import router as r

class TestAPILocally(unittest.TestCase):

    def setUp(self):
        self.client = app.app_context()
        self.client.push()

    def tearDown(self):
        self.client.pop()

    def test_root(self):
        with app.app_context():
            retVal = r.get()
            self.assertTrue('v1' in retVal)

    """def test_root_response(self):
        with app.app_context():
            retVal = r.root_response()
            for var in retVal:
                print(retVal.index(var), var)
            self.assertTrue(retVal[1] == 501)"""

    def test_create_user(self):
        with app.app_context():
            retVal = r.create_user()
            self.assertTrue(retVal[1] == 501)

    def test_read_user(self):
        with app.app_context():
            retVal = r.read_user(1)
            self.assertTrue(retVal[1] == 501)

    def test_update_user(self):
        with app.app_context():
            retVal = r.update_user(1)
            self.assertTrue(retVal[1] == 501)

if __name__ == '__main__':
    unittest.main()