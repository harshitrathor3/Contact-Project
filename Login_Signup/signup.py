from mysql import connector
from constants import host, database, user, password
from Login_Signup import login



try:
    def signup(mob, paswrd, name, email=None, dob=None):
        mydb = connector.connect(host=host, user=user, password=password, database = database)
        cursor = mydb.cursor()

        _, msg, _, _ = login.check_user_exist(mob, paswrd)

        if msg=='User not exist':
            token = None
            qr = "INSERT INTO login VALUES(%s, %s, %s, %s, %s, %s, curdate(), curtime(), curdate(), curtime())"
            cursor.execute(qr, (mob, paswrd, name, token, email, dob))
            mydb.commit()
            ans = 'Signed up successfully'
            status = True
        else:
            ans = "User already exist"
            status = False
        cursor.close()
        mydb.close()
        return status, ans

except connector.Error as err:
    if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except Exception as e:
    print("Other error happened" % (e))