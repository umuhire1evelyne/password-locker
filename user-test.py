import unittest
from user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("evelyne", "umuhire", "0780313525", "umuhire1evelyne@gamil.com")  # create user object

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.users_array = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.first_name, "evelyne")
        self.assertEqual(self.new_user.last_name, "umuhire")
        self.assertEqual(self.new_user.phone_number, "0780313525")
        self.assertEqual(self.new_user.email, "umuhire1evelyne@gamil.com")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
         the users array
        """
        self.new_user.save_user_details()  # saving the new user
        self.assertEqual(len(User.users_array), 1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple users
        to our users_array
        """
        self.new_user.save_user_details()
        test_user = User("Test", "user", "0780313525", "test@user.com")  # new user
        test_user.save_user_details()
        self.assertEqual(len(User.users_array), 2)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(), User.users_array)


if __name__ == '__main__':
    unittest.main()