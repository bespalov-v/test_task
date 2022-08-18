from Crypto.Random import get_random_bytes
from password import accounts
from Crypto.Cipher import AES


class EncryptedData(accounts):
    def __init__(self, base: accounts):
        self.account = ['', '', '']
        self.account[0] = base.account[0]
        self.account[1] = base.account[1]
        self.is_encrypted = False
        self.login_nonce = b'a'
        self.password_nonce = b'b'
        self.data_saved = base.data_saved

    def add_login(self, key):
        while len(self.get_login()) % 16 == 0:
            self.account[0] = self.account[0] + ' '
        encrypt = AES.new(key, AES.MODE_EAX)
        self.login_nonce = encrypt.nonce
        self.account[0] = encrypt.encrypt(self.account[0].encode('utf-8'))

    def add_password(self, key):
        while len(self.get_password()) % 16 == 0:
            self.account[1] = self.account[0] + ' '
        encrypt = AES.new(key, AES.MODE_EAX)
        self.password_nonce = encrypt.nonce
        self.account[1] = encrypt.encrypt(self.account[1].encode('utf-8'))

    def set_key(self, key):
        self.account[2] = key

    def get_key(self):
        return self.account[2]

    def encrypt(self):
        if self.data_saved:
            print('Enter encryption key\'s length.\n Possible options: 16, 24, 32.')
            keylen_is_valid = False
            while not keylen_is_valid:
                key_len = input()
                if key_len == '16' or key_len == '24' or key_len == '32':
                    keylen_is_valid = True
                    key_len = int(key_len)
                else:
                    print('Length is not valid, enter specified length.')
                    print('\n')
            print('\n')
            key = get_random_bytes(key_len)
            self.set_key(key)
            self.add_login(key)
            self.add_password(key)
            print(f'Encryption succesfull. Encrypted data:\nLogin: {self.account[0]}\nPassword: {self.account[1]}\nKey: {self.account[2]}')
            self.is_encrypted = True
            print('\n')
        else:
            print('Enter user information first.')
            print('\n')

    def decrypt(self, base: accounts):
        if self.is_encrypted:
            decrypt_login = AES.new(self.get_key(), AES.MODE_EAX, nonce=self.login_nonce)
            decrypt_password = AES.new(self.get_key(), AES.MODE_EAX, nonce=self.password_nonce)

            decrypted_login = decrypt_login.decrypt(self.get_login()).decode("utf-8")
            decrypted_password = decrypt_password.decrypt(self.get_password()).decode("utf-8")

            print(f'Decrypted data:\nLogin: {decrypted_login}\nPassword: {decrypted_password}')
            print('\n')

            if base.get_login() == decrypted_login and base.get_password() == decrypted_password:
                print(f'Entered login: {base.get_login()}\tEntered password: {base.get_password()}')
                print(f'Decrypted login: {decrypted_login}\tDecrypted password: {decrypted_password}')
                print('Decryption was successful.')
                print('\n')
            else :
                print('Decryption wasn\'t successful')
                print('\n')

        else:
            print('Data hasn\'t been encrypted yet.')
            print('\n')
