# PASSWORD LOCKER

## Built By [Francis Sakwa](https://github.com/FrancisSakwa89/)

## Description
Password Locker is a terminal run python application that allows users to create accounts using their names save,delete,check if they are existing and displaying them

## User Stories
These are the behaviours that the application implements for use by a user.(What the user is able to view or do)

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display guides for navigation | **In terminal: $./run.py** | Hello, Welcome to your Password account. What is your name? (once you enter your name):Use these known short codes to operate : cc -> create account.  dc -> Display your account.  fc ->Find password account.  ex ->exit Password Locker account. |
| Display prompt for creating an account | **Enter: cc** | Enter first name, last name, password  .|
| Display prompt for finding account | **Enter: fc** | Enter the name you want to serach for  |
| **Enter: dc** | Prints a list of saved password account |
| Log out account  | **Enter: ex** | Thanks for your time you have logged out of your account ,BYE! ....|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* Good internet connection
* For windows users:  GitBash
* For linux/ubuntu users : Git


### Cloning
* In your terminal:

        $ git clone https://github.com/FrancisSakwa89/Password-Locker.git
        $ cd Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ ./run.py


## Testing the Application
* To run the tests for the class file and check if it functions well:

        $ python3.5 password_test.py

## Technologies Used
* Python3.5

### LICENSE
[MIT License](https://choosealicense.com/licenses/mit/#)

 __Copyright (c) 2018 Francis Sakwa__|

