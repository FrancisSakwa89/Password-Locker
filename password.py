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

    
    def delete_password(self):

        '''
        delete_password method deletes a saved password from the password_list
        '''

        Password.password_list.remove(self)

    @classmethod
    def find_by_name(cls,first_name):
        '''
        Method that takes in a name and returns a contact that matches that name.

        Args:
            name: first name to search for
        Returns :
            Password of person that matches the name.
        '''

        for password in cls.password_list:
            if password.first_name == first_name:
                return password
    
if __name__ == '__main__':
    unittest.main()    