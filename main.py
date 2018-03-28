import getpass

print("****************************************")
print("*********** Aurin Bank - ATM ***********")
print("****************************************")

user_account = input("Enter your account number: ")
user_password = getpass.getpass("Enter your password: ")

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

if user_account in accounts and user_password == accounts[user_account]['password']:
    print("Welcome {}!".format(accounts[user_account]['name']))
else:
    print("Account or password do not match!")