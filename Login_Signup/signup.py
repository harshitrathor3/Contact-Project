from mysql import connector
from constants import host, database, user, password
from Login_Signup import login



try:
    def signup(mob, paswrd, name, email='', dob=''):
        mydb = connector.connect(host=host, user=user, password=password, database = database)
        cursor = mydb.cursor()

        status, msg = login.check_user_exist(mob, paswrd)

        if msg=='User not exist':
            if email=='':
                email=None
            if dob=='':
                dob=None
            token = None
            qr = "INSERT INTO login VALUES(%s, %s, %s, %s, %s, %s, curdate(), curtime(), curdate(), curtime())"
            cursor.execute(qr, (mob, paswrd, name, token, email, dob))
            mydb.commit()
            ans = 'Signed up successfully.. Now you can login'
            var = True

        else:
            ans = "User already exist.. Pls login via Login Page"
            var = False
        cursor.close()
        mydb.close()
        return var, ans

except connector.Error as err:
    if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except Exception as e:
    print("Other error happened" % (e))