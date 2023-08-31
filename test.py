from mysql import connector

mydb = connector.connect(host = 'localhost', password='', user='root', database='test')
cursor = mydb.cursor()

qr = 'Insert into t values (%s, %s, %s)'

val = [
    [2, 'b', 'b'],
    [3, None, 'c'],
    [4, 'd', None],
    [None, None, None],
]

cursor.executemany(qr, val)
print(cursor.rowcount)
mydb.commit()