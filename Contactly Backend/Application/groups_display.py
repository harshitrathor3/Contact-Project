from mysql import connector
# from ..constants import host, database, user, password
host = 'bkq2iacrckyswhmkbklh-mysql.services.clever-cloud.com'
database = 'bkq2iacrckyswhmkbklh'
user = 'uotwmxtea0c3wyvn'
password = 'uEm0TjBWWEhM0CKPazi5'

try:
    def display_groups(id, token):
        mydb = connector.connect(host=host, user=user, password=password, database = database)
        cursor = mydb.cursor()
        cursor.execute(f"select token from login where id = {id}")
        db_token = cursor.fetchone()[0]
        status = False
        msg = "Invlid Token"
        data = {}
        if db_token!=token:
            return status, msg, data
        cursor.execute(f'SELECT group_id, group_name FROM groupss WHERE id={id}')
        group_id_name = cursor.fetchall()
        
        status = True
        msg = "Success"
        

        for gid, gname in group_id_name:
            data[f'{gid}'] = [gname]

        cursor.execute(f'SELECT mobile_num, name, group_id, email, profession, relation, dob, address, city, pincode, gender FROM contacts WHERE id = {id}')
        
        for d in cursor.fetchall():
            data[f'{d[2]}'].append(d)
        
        cursor.close()
        mydb.close()
        
        return status, msg, data

        
    display_groups('24252', 'e89e356074f43ac4a2f1')
except connector.Error as err:
    if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except Exception as e:
    print("Other error happened" % (e))
