import tkinter
import uuid
import hashlib
import pymysql.cursors


def send_to_db():

    new_user = input('Enter a user name: ')
    new_pass = input('Enter a password:')
    salt = uuid.uuid4()
    salt = str(salt)
    to_encode = new_pass + salt
    user_hash = hashlib.sha256(to_encode.encode())
    print(user_hash)

    connection = pymysql.connect(host='mrbartucz.com',
                                 user='eb1391ck',
                                 password='putty1562',
                                 db='eb1391ck_password_hash',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Select all Students
            sql = "INSERT INTO user_data(user_name, salt, hash) VALUES (%s, %s, %s) "
            to_sql = (new_user, salt, user_hash.hexdigest())

            # execute the SQL command
            cursor.execute(sql, to_sql)

            # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default. Must commit.
            connection.commit()
    finally:
        print('Test your account credentials')
        login()
        connection.close()


def user_login(user, password):
    #user = input('Enter your username: ')
    #password = input('Enter your password:')

    connection = pymysql.connect(host='mrbartucz.com',
                                 user='eb1391ck',
                                 password='putty1562',
                                 db='eb1391ck_password_hash',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            salt = ''      #if db does not find value for salt or hash, makes it so if to_compare == str(user_hash) is to_compare == 0
            user_hash = ''

            sql = "SELECT * FROM user_data WHERE user_name = %s"
            to_sql = user

            cursor.execute(sql, to_sql)

            for row in cursor:
                salt = row['salt']
                user_hash = row['hash']

            salt = str(salt)
            to_encode = password + salt

            result_hash = hashlib.sha256(to_encode.encode())
            to_compare = result_hash.hexdigest()
            # print(to_compare)
            # print(user_hash)
            if to_compare == str(user_hash):
                print('Login Successful')
                return 1
            else:
                print('Login Failed')
                return 0

    finally:
        connection.close()

def print_menu():
    menu_select = 0

    print('Enter 1: To create a new account.')
    print('Enter 2: To login to an existing account.')
    print('Enter 3: to exit')
    menu_select = int(input('Enter Selection: '))
    if menu_select == 1:
        send_to_db()
    if menu_select == 2:
        login()
    if menu_select == 3:
        menu_select = 3


def login_press(e, u):
    print(e)
    print(u)
    return_code = user_login(e, u)
    print(return_code)
    return return_code

def main():
    print_menu()


if __name__ == '__main__':  # for import
    main()
