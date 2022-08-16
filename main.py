from password import  accounts
from encryption import EncryptedData

Base = accounts()
encrypted = EncryptedData(Base)
is_working = True
while is_working:
    print('Enter number:\n1.Enter user\'s information.\n2.Encrypt\n3.Decrypt\n4.Quit' )
    choice = input()
    if choice == '1':
        Base.add_account()
    elif choice == '2':

        encrypted = EncryptedData(Base)
        encrypted.encrypt()
    elif choice == '3':
        encrypted.decrypt(Base)
    elif choice == '4':
        is_working = False
    else:
        print('Choice isn\'t valid.')

