import getpass

print("****************************************")
print("**************Welcome to****************")
print("*********** Aurin Bank - ATM ***********")
print("****************************************")

# Ask the user to type the bank account and password and store it in variables
user_account = input("Enter your account number: ")
user_password = getpass.getpass("Enter your password: ")

# Dictionary with accounts as keys and another dictionary with account data and values
accounts = {
    '0001-02': {
        'password': 'getin', 
        'name': 'John Doe', 
        'active': 1
    }, 
    '0002-02': {
        'password': 'iamgod', 
        'name': 'Jane Doe', 
        'active': 0
    }
}

# Check if the typed account exists in the dictionary AND if the typed password match with the password of that account
if user_account in accounts and user_password == accounts[user_account]['password']:
    # Since the check is ok, greets the user by name(stored in the dictionary)
    print("Welcome {}!".format(accounts[user_account]['name']))
else:
    # Since the check failed, inform the user.
    print("Account or password do not match!")