import pandas as pd
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
# Создаем таблицу
create_query = ("CREATE TABLE IF NOT EXISTS `test`.`Anketa.Question6`")
cur_serv._query(create_query)
# Вставляем содержимое
todb_insert_query = (f'INSERT INTO `Anketa.Question6`')
cur_serv.execute(todb_insert_query)

# #Закрываем соединение
cur_serv.close()
con_serv.commit()
con_serv.close()