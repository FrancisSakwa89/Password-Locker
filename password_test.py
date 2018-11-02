import unittest # Importing the unittest module
from password import Password # Importing the password class

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Password("first_name","last_name","password_input") # create password object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name,"first_name")
        self.assertEqual(self.new_password.last_name,"last_name")
        self.assertEqual(self.new_password.password_input,"password_input")

    def test_save_password(self):
        '''
        test_save_password test case to test if the password object is saved into
         the passowrd list
        '''
        self.new_password.save_password() # saving the new contact
        self.assertEqual(len(Password.password_list),1)

    

if __name__ == '__main__':
    unittest.main()