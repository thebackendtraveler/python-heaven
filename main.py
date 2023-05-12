import dbConfig as myDB
import mysql.connector as mysql
from pprint import pprint

try: 
    conn = mysql.connect(**myDB.dbConfig)
    cursor=conn.cursor()
    
    firstname = input("Enter your firstname: ")
    lastname = input("Enter your lastname: ")
    email = input("Enter your email: ")

    #cursor.execute("SELECT * FROM students")
    #cursor.execute("INSERT INTO students (student_id, first_name) VALUES(5, 'FJ')")
    cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES('{0}','{1}', '{2}')".format(firstname, lastname, email))
    conn.commit()
    #pprint(cursor.fetchall())
    print(conn)

    conn.close()

except mysql.Error as err:
    if err.errno == 1045:
        print("The credentials are not correct, either due to wrong password or username")
    else: 
        print(err)