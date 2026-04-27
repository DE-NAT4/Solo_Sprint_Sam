import json



active_users = []
disabled_users = []

with open("active_users.json" , "r") as factive:
    json_active_string = factive.read()

active_users = json.loads(json_active_string)

with open("disabled_users.json" , "r") as fdisabled:
    json_disabled_string = fdisabled.read()

disabled_users = json.loads(json_disabled_string)


def save_active():
    with open("active_users.json", "w") as file:
        file.write(json.dumps(active_users))


def save_disabled():
    with open("disabled_users.json", "w") as file:
        file.write(json.dumps(disabled_users))


def print_active():
    print ("Active users")
    for user in enumerate(active_users):
        print (user)


def print_disabled():
    print ("Disabled users")
    for user in enumerate(disabled_users):
        print (user)

def print_main_menu():
    print(
    "\n Main menu"
    "\n---------------------------"
    "\n 4 - Test Login "
    "\n 3 - Disable/Enable User" 
    "\n 2 - View Active/Disabled Users" 
    "\n 1 - Add User" 
    "\n 0 - Save and Exit App" 
    "\n---------------------------"
    )


def check_user():
    while True:
        user_check = 1
        test_user = input("Enter your username ")
        for user in active_users:
            if user["username"] == test_user:
                test_pass = input("Enter your password ")
                if user["password"] == test_pass:
                    print("ACCESS GRANTED")
                    return
                else: 
                    print ("Login Failed")
                    return
            else:
                user_check += 1
                if user_check <= len(active_users):
                    continue
                elif user_check > len(active_users):
                    print("Login Failed")
                    return



while True:
    print_main_menu()
    menu_select = input("Please input your command ")

    if menu_select == "0":
        save_active()
        save_disabled()
        break

    elif menu_select == "1":
        while True:
            add_name = input("Please enter the name ")
            add_pass = input("Please enter the password ")
            add_choice = input("Would you like them to be added to disabled list instead? (y/n) ")
            if add_choice == "y":
                disabled_users.append({
                "username" : add_name,
                "password" : add_pass
                })
                print("Added to disabled user list")
                print_disabled()
                break

            elif add_choice == "n":
                active_users.append({
                "username" : add_name,
                "password" : add_pass
                })
                print("Added to active user list")
                print_active()                
                break

            else:
                print("Invalid Input")

    elif menu_select == "2":
        print_active()
        print_disabled()

    elif menu_select == "3":
        while True:
            en_dis_choice = input("Would you like to enable or disable a user? (enable/disable) ") 
            if en_dis_choice == "enable":
                print_disabled()
                if len(disabled_users) == 0:
                    print("WARNING disabled user list is empty returning to menu")
                    break

                else: 
                    try:
                        enable_index_choice = int(input("Please choose the index of the user to enable "))
                        if 0 <= enable_index_choice <+ len(disabled_users):
                            active_users.append(disabled_users[enable_index_choice])
                            disabled_users.pop(enable_index_choice)
                            print("Enabled user")
                            print_active()
                            break
                        else:
                            print("Invalid Input")
                    except:
                        print("Invalid input")

            elif en_dis_choice == "disable":
                print_active()
                if len(active_users) == 0:
                    print("WARNING active user list is empty returning to menu")
                    break

                else: 
                    try:
                        disable_index_choice = int(input("Please choose the index of the user to enable "))
                        if 0 <= disable_index_choice <+ len(active_users):
                            disabled_users.append(active_users[enable_index_choice])
                            active_users.pop(enable_index_choice)
                            print("Disabled user")
                            print_disabled()
                            break
                        else:
                            print("Invalid Input")
                    except:
                        print("Invalid input")
                

            else:
                print("Invalid Input")

    elif menu_select == "4":
        check_user()
                    
                    


    else:
        print ("Invalid Input")