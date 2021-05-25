from numpy import column_stack
import pandas as pd
import MySQLdb
from pandas.core.dtypes.missing import isna
connection_params_sql = {'host': '10.144.198.132',
                         'user': "mon_report_bti",
                         'passwd': "Report_112233",
                         'charset': "utf8",
                         'db': "test"}

# Приводим в порядок заголовки
input_columns = pd.read_excel('Опросник.xlsx', usecols="N:AG", nrows=1 ,skiprows=1)
table_columns = input_columns.values.tolist()
table_columns = str(table_columns).strip("""[']""")
table_columns = str(table_columns).split("""', '""")
for column in table_columns:
    column = column + ' INT'
print(table_columns[0])

# Приводим в порядок ответы
# input_rows = pd.read_excel('Опросник.xlsx', na_values='', usecols="I,N:AG", skiprows=[0,1,2])
# table_rows = input_rows.values.tolist()
# for row in table_rows:
#     for item_index in range(1,len(row)):
#         row[item_index] = 0 if type(row[item_index]) == float else 1
# print (table_rows)
# for row in table_rows:
#     item = str(row).strip('[]')
#     print (f'{item}')

print ('Jobisdone')


#table_rows = (str(table_rows[0]).strip('[]'))
#table_rows.split(',')
# for i in range(len(table_rows)):
#     table_rows[i] = (str(table_rows[i]).strip('[]'))
#     table_rows[i] = (str(table_rows[i]).split(','))
#new_rows = (new_rows.split(','))
#for i in range(len(new_rows))


# table_columns = (str(table_columns)).split(',')
# print(table_columns[2])
#print (str(table_rows).split(',')).strip('[]')
#print (new_array[0])
#print (table_rows[1])



# # Создаем подключение
# con_serv = MySQLdb.connect(**connection_params_sql)
# # устанавливаем курсор
# cur_serv = con_serv.cursor()
# # Создаем таблицу
# create_query = ("CREATE TABLE IF NOT EXISTS `test`.`Anketa.Question6` ")
# print (create_query)
#cur_serv._query(create_query)
# # Вставляем содержимое
# todb_insert_query = (f'INSERT INTO `Anketa.Question6`')
# cur_serv.execute(todb_insert_query)
# print ('Jobisdone')
# # #Закрываем соединение
# cur_serv.close()
# con_serv.commit()
# con_serv.close()