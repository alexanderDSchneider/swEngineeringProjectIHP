import tkinter
import uuid
import hashlib
import pymysql.cursors
#Written by Alexander Schneider 5/3/2020
#Connect to the database and salt and hash passwords

def send_to_db(e, u):
    
    new_user = e
    new_pass = u

    #for salting and hashing passwords 
    salt = uuid.uuid4()
    salt = str(salt)
    to_encode = new_pass + salt
    user_hash = hashlib.sha256(to_encode.encode())

    #connect to db
    connection = pymysql.connect(host='mrbartucz.com',
                                 user='eb1391ck',
                                 password='putty1562',
                                 db='eb1391ck_password_hash',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            #reserved word for comparisons
            if new_user != 'default':
                
                #find if the username is already taken
                sql = "SELECT * FROM user_data WHERE user_name = %s"
                to_sql = new_user
            
                #attempt to find new username in db
                cursor.execute(sql, to_sql)

                #if not found, null string 
                fetched_user = " "

                #fetch username from retrived data    
                for row in cursor:
                    fetched_user = row['user_name']

                
                #if new user is not taken, = to " "
                if new_user != fetched_user:

                    #insert generated credentials with the username into the database          
                    sql = "INSERT INTO user_data(user_name, salt, hash) VALUES (%s, %s, %s) "
                    to_sql = (new_user, salt, user_hash.hexdigest())
                
                    # execute the SQL command
                    cursor.execute(sql, to_sql)

                    # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default. Must commit.
                    connection.commit()
                    return 1

                else:
                    return 0

            else:
                return 3                
            
    finally:
        connection.close()


def user_login(user, password):
    #user = input('Enter your username: ')
    #password = input('Enter your password:')

    #connect to db
    connection = pymysql.connect(host='mrbartucz.com',
                                 user='eb1391ck',
                                 password='putty1562',
                                 db='eb1391ck_password_hash',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            salt = 'default'      #if db does not find value for salt or hash, makes it so if to_compare == str(user_hash) is to_compare == 0
            user_hash = 'default'

            #select data from username
            sql = "SELECT * FROM user_data WHERE user_name = %s"
            to_sql = user

            cursor.execute(sql, to_sql)

            #fetch data from cursor    
            for row in cursor:
                salt = row['salt']
                user_hash = row['hash']

            #for comparing fetched data to entered password
            salt = str(salt)
            to_encode = password + salt

            #rehash for comparison
            result_hash = hashlib.sha256(to_encode.encode())
            to_compare = result_hash.hexdigest()

            print(user_hash)
            print(result_hash)
            
            print(to_compare)
            print(user_hash)
            print(salt)
         
            if to_compare == user_hash:
                if salt != 'default':
                    #success
                    return 1
                else:
                    return 4
            elif salt != 'default':
                #fail, account exists
                return 0
            elif salt == 'default':
                #fail, account does not exist
                return 2

    finally:
        connection.close()


def login_press(e, u):
    return_code = user_login(e, u)
    return return_code

def create_press(e, u):
    return_code = send_to_db(e, u)
    return return_code    
