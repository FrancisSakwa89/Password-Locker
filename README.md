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
| Display guides for navigation | **In terminal: $./run.py** | Hello Welcome to your Pass Word Locker. What is your name? (once you enter your nname):Use these known short codes to operate : SU -> SIGN UP.  DA -> Display your account.  LN ->LOGIN.  ex ->exit Pass Word Locker. |
| Display prompt for creating an account | **Enter: SU** | Enter account name, user name password and email .|
| Display prompt for login in | **Enter: LN** | Enter your account password to login |
| Once logged in | **You are now logged in to your  account** |  Use these short codes:CA -> Create new credential.DC -> Display your credentials list.  ex ->Log out your credentials account. |
| Display prompt for creating a credential | **Enter: CA** | Create new credential, Credential name: and password |
| Display a list of credentials | **Enter: DC** | Prints a list of saved credentials |
| Log out account  | **Enter: ex** | You have logged out your  account |

* To completely interact with this application,you will need to sign up to have an account,then login to your account and work in there.

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* Good internet connection
*  For windows users:  GitBash
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

 __Copyright (c) 2018 Francis Sakwa__
