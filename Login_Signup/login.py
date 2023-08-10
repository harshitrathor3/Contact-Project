from mysql import connector
from constants import host, database, user, password

try:
    def check_user_exist(mob, pasw):
        mydb = connector.connect(host=host, user=user, password=password, database = database)
        cursor = mydb.cursor()
        cursor.execute(f"SELECT password from login where id = '{mob}'")
        ans = cursor.fetchall()
        cursor.close()
        mydb.close()
        if len(ans) == 0:
                return False, 'User not exist'
        elif pasw!=ans[0][0]:
            return False, 'Invalid Password'
        else:
            return True, "Login successfully!"

    if __name__=='__main__':
        # mob = input('Enter your mobile num : ')
        # paswrd = input("Enter your password : ")
        mob = '123456'
        paswrd = 'psw1'

        status, msg = check_user_exist(mob, paswrd)

        if status:
            print(msg)
            mydb = connector.connect(host="localhost", user='root', password="", database = 'contact')
            cursor = mydb.cursor()
            cursor.execute(f"SELECT * FROM contacts WHERE id = '{mob}'")
            for i in cursor.fetchall():
                print(i)
            cursor.execute(f'UPDATE login SET last_login_date=curdate(), last_login_time=curtime() where id = "{mob}"')
            mydb.commit()

            cursor.close()
            mydb.close()
        else:
            print(f'Login failed reason : {msg}')        
except connector.Error as err:
    if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except Exception as e:
    print("Other error happened" % (e))