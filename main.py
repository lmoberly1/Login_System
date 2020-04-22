# Login system for users

# File of user account usernames and passwords
login_file = "users.txt"

# Account creation function
def account_creation_system(user_file):

    # Requesting username and password
    username = raw_input("Create a username: ")
    password = raw_input("Create a password: ")
    verified_password = raw_input("Verify your password: ")

    # Checking to see if username exists
    with open(user_file) as file:
        if username in file.read():
            print("This username is taken. Please try again.")
            quit()

    # Checking if passwords match
    if verified_password != password:
        print ("The passwords do not match. Please try again.")
        quit()
    else:
        print ("Account successfully created.")
        file.close()
        return username, password

# Account login function
def login_system(user_file):

    # User enters existing username and password
    existing_username = raw_input("Enter your username:")
    existing_password = raw_input("Enter your password:")

    # User file is checked to make sure the combination is found
    with open(user_file) as file:
        if ("Username:" + existing_username + "\tPassword:" + existing_password + "\n") in file.read():
            print("Successful Login.")
            print("This is the main page.")
            quit()
        else:
            print("Unsuccessful Login.")
            quit()


# MAIN FUNCTION

# Asks user to login or create new account
user_decision = int(raw_input("To Login: Press 0 \nTo Create New a Account: Press 1\n"))

# Create New Account page
if user_decision == 1:

    # Calls the account_creation function and assigns output to new_username and new_password
    new_username, new_password = account_creation_system(login_file)

    # Adds the new_username and new_password to the user file
    file = open(login_file, "a")
    file.write("Username:" + new_username + "\tPassword:" + new_password + "\n")
    file.close()

    # Calls the login function
    login_system(login_file)

# Login page
elif user_decision == 0:

    # Calls the login function
    login_system(login_file)


# Check for invalid options
else:
    print("This option is not available.")
    quit()
