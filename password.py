class Password:
    """
    Class that generates new instances of passwords
    """

    password_list = [] #Empty password list

    def __init__(self,first_name,last_name,password_input):
      # docstring removed for simplicity

       self.first_name = first_name
       self.last_name = last_name
       self.password_input = password_input
    
      # Init method up here
    def save_password(self):

        '''
        save_password method saves password objects into password_list
        '''

        Password.password_list.append(self)

      # Items up here...

    def test_save_multiple_password(self):
        '''
        test_save_multiple_passowrd to check if we can save multiple password
        objects to our password_list
        '''
        self.new_passowrd.save_passowrd()
        test_password = Password("first_name","last_name","password_input") # new password
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)

if __name__ == '__main__':
    unittest.main()    