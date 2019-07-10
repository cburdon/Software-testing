from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test', "The username does not match the expected value.")
        self.assertEqual(user.password, 'abcd', 'The password does not match the expected value.')
