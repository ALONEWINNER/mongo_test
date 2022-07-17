import mysql.connector as connection    #pip install mysql-connector-python

#communication between pycharm(python) and sql
mydb =connection.connect(host ="localhost",user="root",password="alone")
#mydb =connection.connect(host ="admin url",user="given by company",password="given by company") #when we are working in a company

print(mydb)   #o/p: <mysql.connector.connection_cext.CMySQLConnection object at 0x000001EFF6466CF8>  if getting this .then ok\

#cursor = it is a pointer that
cursor=mydb.cursor()   #create cursor
cursor.execute("show databases")    #execute query
print(cursor.fetchall())

#create a database
#cursor.execute("create database ineuron")
#print(cursor.fetchall())

#use database
#cursor.execute("use ineuron")   #not working here
#cursor.execute("create table ineuron.student(stud_id int(10), stud_name varchar(20),mailid varchar(25),salary int(6),attendence int(3))")
#print(cursor.fetchall())

q2=cursor.execute("select * from ineuron.student")
print(q2)



