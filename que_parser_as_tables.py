from numpy import NaN, column_stack, inner
import numpy as np
import pandas as pd
import re
from sqlalchemy import create_engine
from connection_params import db_creds,db_charset
from file_to_parse import input_file,column_logins,column_question,table_name_example,first_table_number

engine = create_engine(db_creds,encoding=db_charset)

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
    frames.to_sql(tablename,con=engine,if_exists='replace')
    pass

for question in column_question:
    table_name = table_name_example + str(first_table_number)
    InsertQuestionIntoDB(question,table_name)
    first_table_number += 1
    print(table_name,' импортирована.')
