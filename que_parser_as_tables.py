from numpy import NaN, column_stack, inner
import numpy as np
import pandas as pd
from pandas.core import frame
import re
from sqlalchemy import create_engine

engine = create_engine('mysql://mon_report_bti:Report_112233@10.144.198.132/test?charset=utf8mb4',encoding='utf8')
#engine = create_engine(URL(connection_params_sql), encod)
input_file = "C:\\Users\\artur.rakhmanov\\Projects\\DBMagic\\Результаты_руководители.xlsx"
column_logins = 'L'                                                                                         #Столбец логинов
column_question = []                                                                                        #Массив вариантов ответов
# column_question.append ('AI:BJ')
# column_question.append ('BK:BT')
# column_question.append ('BV:CO')
# column_question.append ('CP:DQ')
# column_question.append ('DR:EA')
# column_question.append ('EC:EV')
# column_question.append ('EW:FX')
# column_question.append ('FY:GF')
# column_question.append ('GJ:HK')
# column_question.append ('HT:JX')
# column_question.append ('JY:LD')
# column_question.append ('LE:MI')
# column_question.append ('MJ:OQ')
# column_question.append ('OR:PO')
# column_question.append ('PP:RH')
# column_question.append ('AI:BJ')
# column_question.append ('RI:SY')
# column_question.append ('SZ:UE')
# column_question.append ('UF:VI')
# column_question.append ('VJ:WM')
# column_question.append ('WN:XW')
# column_question.append ('XX:ZY')
# column_question.append ('ZZ:ABG')
# column_question.append ('ABH:ACL')
# column_question.append ('ACM:ADX')
# column_question.append ('ADZ:AER')
# column_question.append ('AEZ:AFA')

column_question.append ('P:AI')
column_question.append ('AJ:BK')
column_question.append ('BL:BS')
column_question.append ('BT:BU')
column_question.append ('BW:CP')
column_question.append ('CQ:DR')
column_question.append ('DS:DZ')
column_question.append ('EA:EB')
column_question.append ('ED:EW')
column_question.append ('EX:FY')
column_question.append ('FZ:GI')
column_question.append ('GK:HL')
column_question.append ('HU:JY')
column_question.append ('JZ:LE')
column_question.append ('LF:MJ')
column_question.append ('MK:OR')
column_question.append ('OS:PP')
column_question.append ('PQ:TB')
column_question.append ('TC:US')
column_question.append ('UT:VY')
column_question.append ('VZ:XC')
column_question.append ('XD:YG')
column_question.append ('YH:ZQ')
column_question.append ('ZR:ABS')
column_question.append ('ABT:ADA')
column_question.append ('ADB:AEF')
column_question.append ('AEG:AFR')
column_question.append ('AFT:AGH')


logins = (pd.read_excel(input_file, usecols=column_logins,header=2, skiprows=0,names=['logins']))          #Получаем логины

def InsertQuestionIntoDB(question_coords, tablename):
    question = (pd.read_excel(input_file, usecols=question_coords, header=2,skiprows=0))
    # Объединяем одинаковые столбцы
    items = question.columns.values.tolist()
    for i in range(len(items)):
        znak = items[i]
        for item in items:
            if znak.upper() == item[:-2].upper():
                question[znak] = question[znak].combine_first(question[item])
                del question[item]
    # Удаляем лишние символы в заголовках столбцов
    items = question.columns.values.tolist()                                                                        # Обновляем массив, так как могли быть удалены столбцы
    for item in range(len(items)):                                                                              # Проверка по регулярке на окончания типа .[0-9$]
        if re.search('\.[0-9]$', items[item]): 
            items[item] = items[item][:-2]
        items[item] = items[item][:64]                                                                          # Обрезаем имя столбца до 64 символов
    question.columns = items
    # Устанавливаем наличие ответов как 1, отсутствие - 0
    question = (question.replace('.*',1,regex=True))
    question = (question.fillna(0))
    question = (question.astype(int))
    # Склеиваем с логинами
    frames = pd.concat([logins,question], axis=1).drop(index=[0])
    # Кладём в бд, или ложим, или складываем, или слаживаем, пох
    frames.to_sql(tablename,con=engine)
    pass


# table_name = 'Anketa.Question'
first_que_number = 6

for question in column_question:
    table_name = 'Anketa.Question.Boss'
    table_name = table_name + str(first_que_number)
    InsertQuestionIntoDB(question,table_name)
    first_que_number += 1
    print(table_name,' импортирована.')
