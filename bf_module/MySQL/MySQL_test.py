import bf_module.MySQL.common as MySQL

mydb = MySQL.connect()

mycursor = mydb.cursor()
mycursor.execute("SELECT value FROM humidity_reads;")

print(mycursor.column_names)
for x in mycursor.fetchall():
  print(x)
  

