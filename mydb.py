import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Balu@123")
cur=con.cursor()
#cur.execute("CREATE DATABASE `AKNU MSN CAMPUS`")
res=cur.execute("SHOW DATABASES")
print(res)
