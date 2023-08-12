from mysql import connector
from os import urandom

from constants import host, database, user, password

try:
    def check_user_exist(mob, pasw):
        mydb = connector.connect(host=host, user=user, password=password, database = database)
        cursor = mydb.cursor()
        cursor.execute(f"SELECT password, name from login where id = '{mob}'")
        ans = cursor.fetchall()
        status = msg = name = token = None
        if len(ans) == 0:
            status = False
            msg = 'User not exist'
                
        elif pasw!=ans[0][0]:
            status = False
            msg = 'Invalid Password'
        else:
            status = True
            msg = 'Login successfully!'
            name = ans[0][1]
            token = urandom(10).hex() # generate 20 random character (hex value)
            cursor.execute(f'UPDATE login SET last_login_date=curdate(), last_login_time=curtime(), token="{token}" where id = "{mob}"')
            mydb.commit()
        cursor.close()
        mydb.close()
        return status, msg, name, token

except connector.Error as err:
    if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except Exception as e:
    print("Other error happened" % (e))