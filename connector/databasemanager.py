import config
import pymysql
import json
import jwt
from datetime import datetime


def connect(db_url, db_name, db_user, db_password):
    cursor = connection.cursor()
    cursor.execute('select * from alert_type')
    data = cursor.fetchall()


def verify_token(user_id, user_token):
    cursor.execute(f"select * from tokens where token ='{user_token}' and user={user_id}")
    return len(cursor.fetchall()) > 0


def send_query(query):
    return True


# TOKEN MANAGEMENT


def get_token(email, password):
    cursor.execute(f"select id from user where email='{email}' and password='{password}'")
    id_user = cursor.fetchone()
    if id_user != 0:
        cursor.execute(f"select token from tokens where user='{id_user[0]}'")
        return cursor.fetchone()
    else:
        return "ERROR"


def create_token(user, email, password):
    cursor.execute(f"select * from `user` where email='{email}' and password='{password}'")
    if len(cursor.fetchall()) > 0:
        # GENERATE JWT TOKEN
        encoded_jwt = jwt.encode({email: str(datetime.now())}, "secret", algorithm="HS256")
        active = 1
        cursor.execute(
            f"INSERT INTO `tokens` (`token`, `date`, `user`, `active`) VALUES ('{encoded_jwt}', NOW(), '{user}', "
            f"'{active}')")
        return encoded_jwt
    else:
        return "ERROR"


def deactivate_token(token):
    cursor.execute(f"UPDATE `tokens` SET `active` = `0` WHERE `tokens`.`token` = '{token}'")


connection = pymysql.connect(host=config.DB_URL, user=config.DB_USER, passwd=config.DB_PASSWORD,
                             database=config.DB_NAME)
cursor = connection.cursor()

# UNIT TESTS


print(verify_token(0, 'aaa'))
print(get_token("a", "0"))
# print(create_token(1, "a", "0"))
