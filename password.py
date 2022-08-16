class accounts:
    def __init__(self):
        self.account = ['', '']
        self.data_saved = False
        self.login_not_valid = True
        self.password_not_valid = True

    def add_login(self, login: str):
        if len(login) > 20 or len(login) < 4:
            print('Login\'s length must be between 4 and 20 characters.')
        else:
        # self.account.update({login: ''})
            self.account[0] = login
            self.login_not_valid = False
            print('Login was saved.')
            print('\n')


    def add_password(self, password):
        if len(password) > 20 or len(password) < 4:
            print('Password\'s length must be between 4 and 20 characters.')
        else:
            self.account[1] = password
            print('Password was saved.')
            print('\n')
            self.password_not_valid = False


    def get_login(self):
        return self.account[0]


    def get_password(self):
        return self.account[1]


    def add_account(self):
        print('Enter login:')
        login = ''
        while self.login_not_valid:
            login = input()
            self.add_login(login)
        print('\n')
        print('Enter password:')
        password = ''
        while self.password_not_valid:
            password = input()
            self.add_password(password)
        self.data_saved = True
        print('\n')


    def print_accounts(self):
        print(self.account)


"""
def add_acount():
    input_login
    input_password
    
    dict.update
    
    // ecrtyption
    dict.update
    
    
    dict(login, password)
    
    print(login, password)
    encryption
    decryption
    print(login, password)
"""
