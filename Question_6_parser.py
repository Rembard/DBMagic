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
table_columns = table_columns.split("""', '""")
#print (table_columns)

# b = 0
# table_columns_for_insert = table_columns
# for index in range(len(table_columns)):
#     table_columns_for_insert[index] = f'`{table_columns[index]}`'
# table_columns_for_insert = tuple(table_columns_for_insert)
# print (f'{table_columns_for_insert}')

# Попытка сделать как по best practices, но с костылём удобней и проще, в итоге выбрал костыль
# for index in range(len(table_columns)):
#     table_columns[index] = f'`{table_columns[index]}` INT'
# table_columns.insert(0 ,'id Int NOT NULL PRIMARY KEY AUTO_INCREMENT')
# table_columns.insert(1, 'logins VARCHAR (120)')
# table_columns = tuple(table_columns)



# Приводим в порядок ответы
input_rows = pd.read_excel('Опросник.xlsx', na_values='', usecols="I,N:AG", skiprows=[0,1,2])
table_rows = input_rows.values.tolist()

# Меняем ответы на бинарные значения
for row in table_rows:
    for item_index in range(1,len(row)):
        row[item_index] = 0 if type(row[item_index]) == float else 1
# Делаем списки ради круглых скобок
for i in range(len(table_rows)):
    table_rows[i] = tuple(table_rows[i])
table_rows = tuple(table_rows)
table_rows =  str(table_rows).strip('()')


# Создаем подключение
con_serv = MySQLdb.connect(**connection_params_sql)
# # устанавливаем курсор
cur_serv = con_serv.cursor()

# С кослытём работает лучше, меньше надо извращатсья
### create_query = (f"CREATE TABLE IF NOT EXISTS `test`.`Anketa.Question6` {table_columns};")

# Создаем таблицу
create_query = ("CREATE TABLE IF NOT EXISTS `test`.`Anketa.Question6` (logins VARCHAR (120), `")

# Костыль для форматирования
n = (len(table_columns)-1)
for i in range(len(table_columns)):
    create_query += table_columns[i]
    if i < n:
        create_query += '` INT, `'
    else:
        create_query += '` INT);'
cur_serv._query(create_query)
print (create_query)


# # Вставляем содержимое
todb_insert_query = (f'INSERT INTO `Anketa.Question6` VALUES ({table_rows})')
print (todb_insert_query)
cur_serv.execute(todb_insert_query)
# #Закрываем соединение
cur_serv.close()
con_serv.commit()
con_serv.close()