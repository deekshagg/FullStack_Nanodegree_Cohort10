import psycopg2

connection = psycopg2.connect('dbname=diksha user=postgres password=root')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True)) # tuple 

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {'id' : 2, 'completed' : False}

cursor.execute(SQL, data) #dictionary

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (3, True)) # tuple 

cursor.execute('SELECT * FROM table2;')

# result = cursor.fetchall()

# print('fetchall=', result)

result = cursor.fetchmany(2)

print('fetchmany(2)=', result)


result2 = cursor.fetchone()

print('fetchone=', result2)

connection.commit()

connection.close()
cursor.close()