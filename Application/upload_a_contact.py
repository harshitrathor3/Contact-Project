from mysql import connector
# from ..constants import host, database, user, password
host = 'bkq2iacrckyswhmkbklh-mysql.services.clever-cloud.com'
database = 'bkq2iacrckyswhmkbklh'
user = 'uotwmxtea0c3wyvn'
password = 'uEm0TjBWWEhM0CKPazi5'

try:
    def upload_contact(json_data):
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
        
        mob = json_data.get('mob', None)
        name = json_data.get('name', None)
        group_id = None
        email = json_data.get("email", None)
        profession = json_data.get("profession", None)
        relation = json_data.get('relation', None)
        dob = json_data.get('dob', None)
        address = json_data.get('address', None)
        city = json_data.get('city', None)
        pincode = json_data.get('pincode', None)
        gender = json_data.get('gender', None)

        qr = "INSERT INTO contacts VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, curdate(), curtime())"
        cursor.execute(qr, (id, mob, name, group_id, email, profession, relation, dob, address, city, pincode, gender))
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
