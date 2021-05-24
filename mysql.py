import MySQLdb
connection_params_sql = {'host': '10.144.198.132',
                         'user': "mon_report_bti",
                         'passwd': "Report_112233",
                         'charset': "utf8",
                         'db': "test"}


# Создаем подключение
con_serv = MySQLdb.connect(**connection_params_sql)
# устанавливаем курсор
cur_serv = con_serv.cursor()
cur_serv._query("CREATE TABLE IF NOT EXISTS test (id Int, Name VARCHAR (20), Fathername VARCHAR (20), Soname VARCHAR (20), Age Int);")
slovar = {'Name':'Рустам','Fathername':'Каримович','Soname':'Гмыря','Age':1}
print (slovar.keys)
print (slovar['Name'])
# age = 1
# while age <= 10:
#     query = (f"INSERT INTO test.test (Name, Fathername, Soname, Age) VALUES ({slovar['Name']}, {slovar['Fathername']}, {slovar['Soname']}, {slovar['Age']});")
#     cur_serv._query(query)
#     age += 1
# cur_serv.execute("""SELECT * FROM `test`;""")

query = (f"INSERT INTO test.test (`Name`, `Fathername`, `Soname`, `Age`) VALUES ('{slovar['Name']}', '{slovar['Fathername']}', '{slovar['Soname']}', {slovar['Age']});")
cur_serv._query(query)
cur_serv.execute("""SELECT * FROM `test`;""")

for s in cur_serv.fetchall():
    print (s)

# output = list(cur_serv.fetchall())
# print(output)

# Сохраняем и закрываем
cur_serv.close()
con_serv.commit()
con_serv.close()

