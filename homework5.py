import os


menu_options = {
    1: 'List all the users',
    2: 'Add a new user',
    3: 'Update the user',
    4: 'Delete the user',
    5: 'Clear the screen',
    6: 'Quit'
}


def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


bmi_users_list = {
    'User 1': {
    'name': 'Julia',
    'age': 41,
    'sex': 'female',
    'height': 175,
    'weight': 58,
    'bmi': 18.93877551020408
    },
    'User 2': {
    'name': 'Domimik',
    'age': 18,
    'sex': 'male',
    'height': 180,
    'weight': 72,
    'bmi': 22.22222222222222
    },
}


def option_list():
    for key, value in bmi_users_list.items():
        print(key, value)


def option_add():
    while True:
        new_user = input("Enter a new user id: ")
        if bmi_users_list.get(new_user):
            print("Choose another id!")
        else:
            break


    new_name_value = input("Enter a user name: ")
    new_age_value = input("Enter a user age: ")
    new_sex_value = input("Enter a user sex: ")
    new_height_value = float(input("Enter a user height (cm): "))
    bmi_height = new_height_value/100
    new_weight_value = float(input("Enter a user weight (kg): "))
    new_bmi_value = new_weight_value/(pow(bmi_height, 2))


    bmi_users_list[new_user] = {
        'name': new_name_value,
        'age': new_age_value,
        'sex': new_sex_value,
        'height': new_height_value,
        'weight': new_weight_value,
        'bmi': new_bmi_value
        }    


def option_update():
    print("Example of how to update:\n"
          "1) a key yo want to change: name\n"\
          "2) a user id you want to change: User 1\n"\
          "3) an updated value: Mary\n")
   
    while True:
        user_key = input('Enter a user id you want to change: ')
        if user_key not in bmi_users_list:
            print("Choose another id!")
        else:
            break


    while True:
        update_key = input('Enter a key you want to change (name, age, sex, height, etc): ')
        if update_key not in bmi_users_list[user_key]:
            print("There is no key like this! Try again")
        else:
            break


    if update_key == 'name':
        update_value = input('Enter an updated value: ')
        bmi_users_list[user_key]['name'] = update_value
    elif update_key == 'age':
        update_value = input('Enter an updated value: ')
        bmi_users_list[user_key]['age'] = update_value
    elif update_key == 'sex':
        update_value = input('Enter an updated value: ')
        bmi_users_list[user_key]['sex'] = update_value
    elif update_key == 'bmi':
        print("Enter updated height and weight because bmi changes, if one of the variables changes")
        update_height = float(input("Enter updated height: "))
        update_weight = float(input("Enter updated weight: "))
        bmi_users_list[user_key]['height'] = update_height
        bmi_users_list[user_key]['weight'] = update_weight
        update_bmi = update_weight/(pow((update_height/100), 2))
        bmi_users_list[user_key]['bmi'] = update_bmi
    elif update_key == 'height':
        print("Enter updated height and weight because bmi changes, if one of the variables changes")
        update_height = float(input("Enter updated height: "))
        update_weight = float(input("Enter updated weight: "))
        bmi_users_list[user_key]['height'] = update_height
        bmi_users_list[user_key]['weight'] = update_weight
        update_bmi = update_weight/(pow((update_height/100), 2))
        bmi_users_list[user_key]['bmi'] = update_bmi
    elif update_key == 'weight':
        print("Enter updated height and weight because bmi changes, if one of the variables changes")
        update_height = float(input("Enter updated height: "))
        update_weight = float(input("Enter updated weight: "))
        bmi_users_list[user_key]['height'] = update_height
        bmi_users_list[user_key]['weight'] = update_weight
        update_bmi = update_weight/(pow((update_height/100), 2))
        bmi_users_list[user_key]['bmi'] = update_bmi


def option_delete():
    user_delete = input('Enter a user id you want to delete: ')
    bmi_users_list.pop(user_delete)


def clear_all():
    os.system('cls')


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = input('Enter your choice: ')
        except:
            print('Wrong input. Please try again...')
        if option == '1':
           option_list()
        elif option == '2':
            option_add()
        elif option == '3':
            option_update()
        elif option == '4':
            option_delete()
        elif option == '5':
            clear_all()
        elif option == '6':
            break
