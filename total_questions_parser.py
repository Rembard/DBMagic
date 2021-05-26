from numpy import column_stack
import pandas as pd
import MySQLdb
from pandas.core.dtypes.missing import isna
connection_params_sql = {'host': '10.144.198.132',
                         'user': "mon_report_bti",
                         'passwd': "Report_112233",
                         'charset': "utf8",
                         'db': "test"}

input_file = "C:\\Users\\artur.rakhmanov\\Projects\\DBMagic\\Результаты_все_сотрудники.xlsx"
input_columns_que = []

que6_coords = 'O:AH'

input_columns_que.append (pd.read_excel(input_file, usecols=que6_coords, nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="AI:BJ", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="BK:BT", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="BV:CO", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="CP:DQ", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="DR:EA", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="EC:EV", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="EW:FX", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="FY:GF", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="GJ:HK", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="HT:JX", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="JY:LD", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="LE:MI", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="MJ:OQ", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="OR:PO", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="PP:RH", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="AI:BJ", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="RI:SY", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="SZ:UE", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="UF:VI", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="VJ:WM", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="WN:XW", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="XX:ZY", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="ZZ:ABG", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="ABH:ACL", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="ACM:ADX", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="ADZ:AER", nrows=1 ,skiprows=1))
# input_columns_que.append (pd.read_excel(input_file, usecols="AEZ:AFA", nrows=1 ,skiprows=1))
# table_columns = input_columns_que12.values.tolist()
# print (table_columns)

# Приводим в порядок заголовки, парсим их
def parse_columns(raw_columns):
    raw_columns = raw_columns.values.tolist()
    raw_columns = str(raw_columns).strip("""[]""")
    raw_columns = raw_columns.split("""', '""")
    for index in range(len(raw_columns)):
        raw_columns[index] = f'`{raw_columns[index][:64]}` INT'
    raw_columns.insert(0, '`logins` VARCHAR (120)')
    table_columns = ','.join(raw_columns)
    return table_columns
#input_columns_que[0] = parse_columns(input_columns_que[0])
#print (input_columns_que[0])
# for i in range(len(input_columns_que)):
#     input_columns_que[i] = parse_columns(input_columns_que[i])
#     print (input_columns_que[i])




# MySQL
# Создаем подключение
con_serv = MySQLdb.connect(**connection_params_sql)
# устанавливаем курсор
cur_serv = con_serv.cursor()
# Создаем таблицы
question_number = 6
for i in range(len(input_columns_que)):
    input_columns_que[i] = parse_columns(input_columns_que[i])
    table_name = 'Anketa.Question'
    table_name +=str(question_number)
    create_query = (f"CREATE TABLE IF NOT EXISTS `test`.`{table_name}` ({input_columns_que[i]});")
    question_number +=1
    print(create_query)
    #cur_serv._query(create_query)



# Закрываем соединение
cur_serv.close()
con_serv.commit()
con_serv.close()