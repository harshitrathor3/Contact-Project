from mysql import connector
from time import sleep

from constants import host, database, user, password

queries = ['''CREATE TABLE login(
    id VARCHAR(10),
    password VARCHAR(30) NOT NULL,
    name VARCHAR(50) NOT NULL,
    token VARCHAR(50) UNIQUE,
    email VARCHAR(50) UNIQUE,
    dob DATE,
    creation_date DATE NOT NULL,
    creation_time TIME NOT NULL,
    last_login_date DATE NOT NULL,
    last_login_time TIME NOT NULL,
    PRIMARY KEY (id)
);''',
'''CREATE TABLE groupss(
    group_id VARCHAR(15),
    id VARCHAR(10) NOT NULL,
    group_name VARCHAR(25) NOT NULL,
    group_scope ENUM('public', 'private') NOT NULL,
    shared_with VARCHAR(100),
    creation_date DATE NOT NULL,
    creation_time TIME NOT NULL,
    last_access_date DATE NOT NULL,
    last_access_time TIME NOT NULL,
    PRIMARY KEY (group_id),
    CONSTRAINT fk_groups_id FOREIGN KEY(id) REFERENCES login(id) ON UPDATE CASCADE,
    UNIQUE (id, group_name)
);''',
'''CREATE TABLE contacts(
    id VARCHAR(10) NOT NULL,
    mobile_num VARCHAR(10) NOT NULL,
    name VARCHAR(50) NOT NULL,
    group_id VARCHAR(15),
    email VARCHAR(50),
    profession VARCHAR(40),
    relation VARCHAR(20),
    dob DATE,
    address VARCHAR(50),
    city VARCHAR(25),
    pincode INT,
    gender ENUM('m', 'f', 'o'),
    creation_date DATE NOT NULL,
    creation_time TIME NOT NULL,
    PRIMARY KEY (id, mobile_num),
    CONSTRAINT fk_contacts_id FOREIGN KEY(id) REFERENCES login(id) ON UPDATE CASCADE,
    CONSTRAINT fk_contacts_group_id FOREIGN KEY(group_id) REFERENCES groupss(group_id),
    UNIQUE (id, mobile_num, group_id)
);''',
"INSERT INTO login VALUES('123456', 'psw1', 'name1', null, 'email1', '2002-05-03',curdate(), curtime(), curdate(), curtime())",
"INSERT INTO login VALUES('12323456', 'psw2', 'name2', null, 'email2', '2003-01-13',curdate(), curtime(), curdate(), curtime())",
"INSERT INTO login VALUES('324252', 'psw3', 'name3', null, 'email3', '1987-03-23',curdate(), curtime(), curdate(), curtime())",
"INSERT INTO login VALUES('24252', 'psw4', 'name4', null, 'email4', '1995-09-19',curdate(), curtime(), curdate(), curtime());",
"INSERT INTO login VALUES('523523', 'psw5', 'name5', null, 'email5', '2000-07-03',curdate(), curtime(), curdate(), curtime());",
"INSERT INTO groupss VALUES('gid1', 123456, 'gname1', 'private', '', curdate(), curtime(), curdate(), curtime())",
"INSERT INTO groupss VALUES('gid2', 123456, 'gname2', 'private', '', curdate(), curtime(), curdate(), curtime())",
"INSERT INTO groupss VALUES('gid3', 123456, 'gname3', 'private', '', curdate(), curtime(), curdate(), curtime())",
"INSERT INTO groupss VALUES('gid4', 24252, 'gname2', 'public', '', curdate(), curtime(), curdate(), curtime())",
"INSERT INTO groupss VALUES('gid5', 24252, 'gname1', 'private', '', curdate(), curtime(), curdate(), curtime())",
"INSERT INTO contacts(id, mobile_num, name, creation_date, creation_time) VALUES('123456', '7289564', 'name1', curdate(), curtime())",
"INSERT INTO contacts(id, mobile_num, name, creation_date, creation_time) VALUES('123456', '789456', 'name2', curdate(), curtime())",
"INSERT INTO contacts(id, mobile_num, name, creation_date, creation_time) VALUES('24252', '7289564', 'name3', curdate(), curtime())",
"INSERT INTO contacts(id, mobile_num, name, creation_date, creation_time) VALUES('24252', '789564', 'name4', curdate(), curtime())",
"update contacts set group_id='gid1' where id='123456'",
"update contacts set group_id='gid1' where mobile_num='789564'",
"update contacts set group_id='gid3' where mobile_num='7289564'"]


try:
    
    if __name__=='__main__':
        mydb = connector.connect(host=host, user=user, password=password, database = database)
        # mydb = connector.connect(host='localhost', user='root', password='', database = 'temp')

        cursor = mydb.cursor()
        cnt=1
        # for query in queries:
        #     cursor.execute(query)
        #     print(f'{cnt} done')
        #     cnt+=1
        #     sleep(2)
        cursor.execute("show tables")
        ans = cursor.fetchall()
        mydb.commit()
        cursor.close()
        mydb.close()

        for i in ans:
            print(i)
       
       
except connector.Error as err:
    if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except Exception as e:
    print("Other error happened" % (e))