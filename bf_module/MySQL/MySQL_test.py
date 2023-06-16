import bf_module.MySQL.common as MySQL

mydb = MySQL.connect()

mycursor = mydb.cursor()

# mycursor.callproc("GetSensorReport",(0,))
mycursor.callproc("GetLastSensorDataByTopic",("esp32_1",0))

for sr in mycursor.stored_results():
    print(sr.column_names)
    for x in sr.fetchall():
        print(x)

# mydb = MySQL.connect()
# mycursor = mydb.cursor()
# mycursor.callproc("InsertSensorReading",("esp32_dguidgd",800,"AA",))
# mydb.commit()
