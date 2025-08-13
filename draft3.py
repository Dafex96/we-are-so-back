newPassword = input("Enter a new password: ")

password = input("Enter your password: ")

while password != newPassword:
    print("The password is incorrect, try again: ")
    password = input("Enter your password: ")
else:
    print("The password is correct.")