from numpy import NaN, column_stack, inner
import numpy as np
import pandas as pd
from pandas.core import frame
# import MySQLdb
# from pandas.core.dtypes.missing import isna
# connection_params_sql = {'host': '10.144.198.132',
#                          'user': "mon_report_bti",
#                          'passwd': "Report_112233",
#                          'charset': "utf8",
#                          'db': "test"}

input_file = "C:\\Users\\artur.rakhmanov\\Projects\\DBMagic\\Результаты_все_сотрудники.xlsx"

column_logins = 'I'
#column_queue6 = 'SE:SI'
column_queue6 = 'SD:SI' #тестовая колонка

logins = (pd.read_excel(input_file, usecols=column_logins,header=2, skiprows=0,names=['blogins']))          #Получаем логины
que6 = (pd.read_excel(input_file, usecols=column_queue6, header=2,skiprows=0))
logins.columns = ['logins123']
#que6 = que6.values.tolist()
items = que6.columns.values.tolist()
split_items = []
for i in range(len(items)):
    znak = items[i]
    for item in items:
        if znak.upper() == item[:-2].upper():
            que6[znak] = que6[znak].combine_first(que6[item])
            del que6[item]
items = que6.columns.values.tolist()                                                                        # Обновляем массив, так как могли быть удалены столбцы
# que6['#ospf'] = que6['#ospf'].combine_first(que6["#OSPF.1"])
que6 = (que6.replace('.*',1,regex=True))
que6 = (que6.fillna(0))
que6 = (que6.astype(int))
frames = pd.concat([logins,que6], axis=1).drop(index=[0])
print (frames)
#print (que6.columns)
#print (que6)
#print(logins)




