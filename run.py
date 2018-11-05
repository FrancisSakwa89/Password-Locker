#!/usr/bin/env python3.6
from password import Password

def create_password(fname,lname,password_input):
   '''
   Function to create a new password
   '''
   new_password = Password(fname,lname,password_input)
   return new_password

def save_password(password):
   '''
   Function to save password
   '''
   password.save_password()

def del_password(password):
   '''
   Function to delete a password
   '''
   password.delete_password()


def find_password(first_name):
   '''
   Function that finds a password by name and returns the password
   '''
   return Password.find_by_first_name(first_name)
def check_existing_password(first_name):
   '''
   Function that check if a password exists with that name and return a Boolean
   '''
   return Password.password_exist(first_name)
def display_password():
   '''
   Function that returns all the saved password
   '''
   return Password.display_passwords()




def main():
   print("Hi welcome to your Password account. What is your name?")
   user_name = input()

   print(f"Hi {user_name}. Do you want to do anything?")

   print('\n')

   while True:
       print("Use these short codes : cc - create a new account, dc - display accounts, fc -find an account, ex -exit the password acount list ")

       short_code = input().lower()

       if short_code == 'cc':
           print("New Account")
           print("-"*10)

           print ("First name ....")
           f_name = input()

           print("Last name ...")
           l_name = input()

        #    print("Email ")
        #    email = input()

           print("Password")
           password_input = input()


           save_password(create_password(f_name,l_name,password_input))
           print ('\n')
           print(f"New Account {f_name} {l_name} {password_input} created")
           print ('\n')

       elif short_code == 'dc':

           if display_password():
               print("Here is a list of all your Account details")
               print('\n')

               for password in display_password():
                   print(f"{password.first_name} {password.last_name} ..... {password.password_input}")

               print('\n')
           else:
               print('\n')
               print("You dont seem to have any details in your account saved yet")
               print('\n')

       elif short_code == 'fc':

           print("Enter the name,password you want to search for")

           search_first_name = input()
           if check_existing_password(search_first_name):
               search_password = find_password(search_first_name)
               print(f"{search_password.first_name} {search_password.last_name} {search_password.password_input}")
               print('-' * 20)

               print(f"password.......{search_password._password_input}")
               print(f"First name.......{search_password.first_name}")
           else:
               print("Those details does not seem to exist")

       elif short_code == "ex":
           print("Thanks for your time you have logged out of your acccount ,BYE! .......")
           break
       else:
           print("The server. Please use the short codes")
if __name__ == '__main__':

   main()