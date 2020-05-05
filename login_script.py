import tkinter
import uuid
import hashlib
import pymysql.cursors
#Written by Alexander Schneider 5/3/2020
#Connect to the database and salt and hash passwords

def send_to_db(e, u):

    new_user = e
    new_pass = u
    salt = uuid.uuid4()
    salt = str(salt)
    to_encode = new_pass + salt
    user_hash = hashlib.sha256(to_encode.encode())

    connection = pymysql.connect(host='mrbartucz.com',
                                 user='eb1391ck',
                                 password='putty1562',
                                 db='eb1391ck_password_hash',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            #find if the username is already taken
            sql = "SELECT * FROM user_data WHERE user_name = %s"
            to_sql = new_user
            print(new_user)

            cursor.execute(sql, to_sql)
                
            for row in cursor:
                fetched_user = row['user_name']

            print(fetched_user)    

            if(new_user != fetched_user):
                          
                sql = "INSERT INTO user_data(user_name, salt, hash) VALUES (%s, %s, %s) "
                to_sql = (new_user, salt, user_hash.hexdigest())
                print("fuck")
                # execute the SQL command
                cursor.execute(sql, to_sql)

                # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default. Must commit.
                connection.commit()
                return 1

            else:
                return 0
            
    finally:
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


def login_press(e, u):
    return_code = user_login(e, u)
    return return_code

def create_press(e, u):
    return_code = send_to_db(e, u)
    return return_code    
#def main():
    #print_menu()


#if __name__ == '__main__':  # for import
    #main()
