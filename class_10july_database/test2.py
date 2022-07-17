import mysql.connector as connection
mydb =connection.connect(host ="localhost",user="root",password="alone")

print(mydb)
cursor=mydb.cursor()   #create cursor
cursor.execute("insert into ineuron.student values(101,'shubham chaudhary','drsn@gmail.com',100,20)")
mydb.commit()  # i will
cursor.execute("select * from ineuron.student")
#print(cursor.fetchall())
for i in cursor.fetchall():
    print(i)