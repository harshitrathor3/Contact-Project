from mysql import connector
# from ..constants import host, database, user, password
host = ''
database = ''
user = ''
password = ''

try:
    def display_contacts(id, token):
        mydb = connector.connect(host=host, user=user, password=password, database = database)
        cursor = mydb.cursor()
        cursor.execute(f"select token from login where id = {id}")
        db_token = cursor.fetchone()[0]
        status = False
        msg = "Invlid Token"
        json_data = {}
        if db_token!=token:
            return status, msg, json_data
        cursor.execute(f"Select mobile_num, name, email, profession, relation, dob, address, city, pincode, gender from contacts where id = {id}")
        data_rows = cursor.fetchall()
        status = True
        msg = "Success"
        cursor.close()
        mydb.close()
        return status, msg, data_rows
    # print(display_contacts('123456', 'c42824e830a1836b9623'))
except connector.Error as err:
    if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except Exception as e:
    print("Other error happened" % (e))
