"""
Name: Arush
Description: Login/Signup program. It was coded in VSCode instead of codehs since codehs wasn't properly storing the .csv file.
"""
import pandas as pd
import string, time, random
attempts = [3]
status = [False]
def check_password_strength():
    password = input("Create your secure password: ")
    is_strong = False
    while is_strong == False:
        if len(password)<8:
            print("You need atleast 8 characters!")
        if any(p.isupper() for p in password) != True:
            print("Atleast 1 uppercase letter!")
        if any(a.islower() for a in password)!= True:
            print("Atleast 1 lowercase letter!")
        if any(s.isdigit() for s in password)!= True:
            print("Atleast 1 number!")
        if any(d in string.punctuation for d in password)!= True:
            print("Atleast 1 special character")
        if len(password)>=8 and any(p.isupper() for p in password) and any(a.islower() for a in password) and any(s.isdigit() for s in password) and any(d in string.punctuation for d in password):
            is_strong = True
        else:
            password = input("Create your secure password: ")
    return password
def check_username_dupe():
    df = pd.read_csv('db.csv')
    uname = input("\nCreate your username: ")
    value_to_check = uname
    column_name = 'username'
    checkName = (df[column_name] == value_to_check).any()
    while checkName:
        uname = input("Your username wasn't unique!\nCreate your username: ")
        value_to_check = uname
        checkName = (df[column_name] == value_to_check).any()
        df = pd.read_csv("db.csv")
    return uname
def createAccount():
    print("\nWe are going to create an account")
    new_data = pd.DataFrame({
        'username': [check_username_dupe()],
        'password': [check_password_strength()]
    })
    new_data.to_csv('db.csv', mode='a', header=False, index=False)
    print("Saving your info...\n")
    time.sleep(1.5)
def checkAccount():
    data = pd.read_csv('db.csv')
    username = input("\nUsername: ")
    password = input("Password: ")
    print("Checking your data...\n")
    time.sleep(1)
    value = attempts[0]
    value -= 1
    attempts[0] = value
    for index in range(0, len(data)):
        if username == data.username[index]:
            if password == data.password[index]:
                print("Password Valid!\nYou are logged in!\nUsername: " + username + "\nAccount Balance: " + str(random.randint(0, 1000000)) + "\n")
                status[0] = True
            else:
                print("Invalid password. " + str(attempts[0]) + " attempts left")
        if (index == len(data)-1) and status[0] == False:
            print("Account doesn't exist")
def main():
    value = input("1. Login\n2. Create Account\n3. Quit\nChoose Option: ")
    while True:
        match value:
            case "1":
                if status[0] == True:
                    value = input("\nYou have been logged out\n1. Login\n2. Create Account\n3. Quit\nChoose Option: ")
                    status[0] = False
                    continue
                if attempts[0] > 0: 
                    if status[0] == False:
                        checkAccount()
                        if status[0] == True:
                            attempts[0] = 3
                            value = input("1. Logout\n2. Create Account\n3. Quit\nChoose Option: ")
                elif (attempts[0] > 0)!= True :
                    print("Too many attempts! Try again after a 15 second cooldown!")
                    time.sleep(15)
                    placeholder = 3
                    attempts[0] = placeholder
            case "2":
                if status[0] == False:
                    createAccount()
                    value = input("1. Login\n2. Create Account\n3. Quit\nChoose Option: ")
                else:
                    value = input("You must be logged out to create an account!\n1. Logout\n2. Create Account\n3. Quit\nChoose Option: ")
            case "3":
                attempts[0] = 3
                status[0] = False
                print("\nQuitting...")
                break
            case _:
                value = input("\nPlease enter a valid option!\n1. Login\n2. Create Account\n3. Quit\nChoose Option: ")
main()