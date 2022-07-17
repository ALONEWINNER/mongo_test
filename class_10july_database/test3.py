import mysql.connector as connection
mydb =connection.connect(host ="localhost",user="root",password="alone")

print(mydb)
cursor=mydb.cursor()
cursor.execute("select stud_id,mailid from ineuron.student")
'''for i in cursor.fetchall():
    print(i)
    print(type(i))'''

l = []
for i in cursor.fetchall():
    l.append(i)



print(l)
#print(type(l[0]))