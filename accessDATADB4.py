import mysql.connector
mydb=mysql.connector.connect(host=”hostname_here”,user=”username”,password=”password_here”)
cursor=mydb.cursor()
#execute query
mycursor.execute(“QUERY_HERE”)
#commiting confirms the changes to the database
mydb.commit()