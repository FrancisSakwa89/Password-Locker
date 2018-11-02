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

if __name__ == '__main__':
    unittest.main()    