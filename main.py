import getpass

print("****************************************")
print("*********** Aurin Bank - ATM ***********")
print("****************************************")

account = input("Enter your account number: ")
password = getpass.getpass("Enter your password: ")

print("Account: {} - Password: {}".format(account, password))