import getpass

print("")
print("****************************************")
print("************** Welcome to **************")
print("*********** Aurin Bank - ATM ***********")
print("****************************************")
print("")

# Ask the user to type the bank account and password and store it in variables
user_account = input("Enter your account number: ")
user_password = getpass.getpass("Enter your password: ")

# Dictionary with accounts as keys and another dictionary with account data and values
accounts = {
    '0001-02': {
        'password': 'getin', 
        'name': 'John Doe',
        'balance': 5000, 
        'active': 1
    }, 
    '0002-02': {
        'password': 'iamgod', 
        'name': 'Jane Doe',
        'balance': 12500, 
        'active': 0
    }
}

# Check if the typed account exists in the dictionary AND if the typed password match with the password of that account
if user_account in accounts and user_password == accounts[user_account]['password']:
    # Since the check is ok, greets the user by name(stored in the dictionary)
    print("****************************************")
    print("*********** Aurin Bank - ATM ***********")
    print("****************************************")
    print("")
    print("Welcome {}!".format(accounts[user_account]['name']))
    op_message = "Type the number correspondent to the operation you wish to execute:"
    op_message += "\n---------------"
    op_message += "\n|1 - Balance  |"
    op_message += "\n|2 - Deposit  |"
    op_message += "\n|3 - Withdraw |"
    op_message += "\n|4 - Exit     |"
    op_message += "\n---------------"
    op_message += "\nOperation: "
    user_op = input(op_message)
else:
    # Since the check failed, inform the user.
    print("Account or password do not match!")