from mysql import connector
# from ..constants import host, database, user, password
host = ''
database = ''
user = ''
password = ''

try:
    def upload(json_data):
        mydb = connector.connect(host=host, user=user, password=password, database = database)
        cursor = mydb.cursor()
        id = json_data.get('id', None)
        token = json_data.get("token", None)
        cursor.execute(f"select token from login where id = {id}")
        db_token = cursor.fetchone()[0]
        status = False
        msg = "Invlid Token"
        
        token = json_data['token']
        if db_token!=token:
            return status, msg

        print(json_data['data'])
        # {'id': 123456, 'token': 'abcdef', 'data': [
        #         ('d1', 'd2', 'd3'), #row 1
        #         ('d1', 'd2', 'd3'), #row 2
        #         ('d1', 'd2', 'd3'), #row 3
        #     ]
        # }

        qr = "INSERT INTO contacts VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, curdate(), curtime()) "
        cursor.executemany(qr, json_data['data'])
        
        mydb.commit()
        msg = 'Contact Updated'
        status = True
        cursor.close()
        mydb.close()
        return status, msg
    

    
except connector.Error as err:
    if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except Exception as e:
    print("Other error happened" % (e))
