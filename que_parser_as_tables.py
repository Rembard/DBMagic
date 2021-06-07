from numpy import NaN, column_stack, inner
import numpy as np
import pandas as pd
import re
from sqlalchemy import create_engine
from connection_params import db_creds,db_charset
from file_to_parse import input_file,column_logins,column_question,column_questions_answer_rpg_style,column_questions_one_answer,table_name_example

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

def InsertSingleAnswerQueIntoDB(question_coords, tablename):
    single_answer_question = (pd.read_excel(input_file, usecols=question_coords, header=2,skiprows=0,names=['answer']))
    result_table = pd.concat([logins,single_answer_question], axis=1).drop(index=[0])
    result_table.to_sql(tablename,con=engine,if_exists='replace')
    
for question in column_question:
    table_name = table_name_example + str(question[1])
    InsertQuestionIntoDB(question[0],table_name)
    print(table_name,' импортирована.')

for question in column_questions_one_answer:
    table_name = table_name_example + str(question[1])
    InsertSingleAnswerQueIntoDB(question[0],table_name)
    print(table_name,' импортирована.')

rpg_style_questions = (pd.read_excel(input_file, usecols=column_questions_answer_rpg_style[0], header=2,skiprows=0))
rpg_style_questions = (rpg_style_questions.fillna(0).astype(int))
rpg_stype_table = pd.concat([logins,rpg_style_questions], axis=1).drop(index=[0])
rpg_stype_table_name = table_name_example + str(column_questions_answer_rpg_style[1])
rpg_stype_table.to_sql(rpg_stype_table_name,con=engine,if_exists='replace')
