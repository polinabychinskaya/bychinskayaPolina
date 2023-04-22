admin_login = 1234
input_login = int(input("Enter your login: "))
bank_accounts = {'User 1': '100$',
                 'User 2': '200$',
                 'User 3': '300$',
                 'User 4': '400$',
                 'User 5': '500$'}
try:
    #Decorator
    def check_valid(fn):
        def wrapper():
            if input_login == admin_login:
                result = fn()
            return result
        return wrapper


    #Decorated function
    @check_valid
    def show_bank():
        print("Bank accounts of all users:")
        for key, value in bank_accounts.items():
            print(key, value)
    show_bank()
except:
    print("You're not an administrator. Access restricted! Try again!")
