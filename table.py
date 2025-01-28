import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Balu@123",database="AKNU MSN CAMPUS")
cur=con.cursor()
cur.execute("""
CREATE TABLE result (
    htno INT PRIMARY KEY,
    name VARCHAR(20),
    telugu INT,
    hindi INT,
    english INT,
    maths INT,
    physics INT,
    chemistry INT,
    social INT,
    total int,avg int,grade varchar(20)  
)
""")
print("create table successfuly")
con.commit()
con.close()