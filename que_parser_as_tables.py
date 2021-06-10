from numpy import NaN, column_stack, inner
import numpy as np
import pandas as pd
import re
from classes import *
from file_to_parse import *
from sqlalchemy import create_engine
from connection_params import db_creds,db_charset

engine = create_engine(db_creds,encoding=db_charset)

stuff_logins = (pd.read_excel(input_file_stuff, usecols=column_logins_stuff,header=2, skiprows=0,names=['logins']))          #Получаем логины
# dop_link = (pd.read_excel(input_file, usecols='E',header=2, skiprows=0,names=['Источник ответа']))
# dop_link['Источник ответа'] = dop_link['Источник ответа'].str[13:]
# logins = pd.concat([logins,dop_link],axis=1)
# print (logins)

def InsertQuestionIntoDB():
    chief_logins = (pd.read_excel(input_file_chief, usecols=column_logins_chief,header=2, skiprows=0,names=['logins']))          #Получаем логины
    for question in column_question_chief:
        obj_question = DataFrame(input_file_chief,question[0], 2 ,0)
        obj_question = pd.concat([chief_logins,obj_question.transquetobin()], axis=1).drop(index=[0])
        table_name = table_name_chief_example+str(question[1])
        obj_question.to_sql(table_name,con=engine,if_exists='replace')
        print (table_name,' импортирована')

def InsertSingleAnswerQueIntoDB():
    chief_logins = (pd.read_excel(input_file_chief, usecols=column_logins_chief,header=2, skiprows=0,names=['logins']))          #Получаем логины
    for question in column_question_chiefs_one_answer:
        obj_question = DataFrame(input_file_chief,question[0], 2 ,0)
        obj_question = pd.concat([chief_logins,obj_question.createanswer()], axis=1).drop(index=[0])
        table_name = table_name_chief_example+str(question[1])
        obj_question.to_sql(table_name,con=engine,if_exists='replace')
        print (table_name, ' импортирована')
#InsertQuestionIntoDB()
InsertSingleAnswerQueIntoDB()
#     question = (pd.read_excel(input_file, usecols=question_coords, header=2,skiprows=0))
#     # Объединяем одинаковые столбцы
#     items = question.columns.values.tolist()
#     for i in range(len(items)):
#         znak = items[i]
#         for item in items:
#             if znak.upper() == item[:-2].upper():
#                 question[znak] = question[znak].combine_first(question[item])
#                 del question[item]
#     # Удаляем лишние символы в заголовках столбцов
#     items = question.columns.values.tolist()                                                                        # Обновляем массив, так как могли быть удалены столбцы
#     for item in range(len(items)):                                                                              # Проверка по регулярке на окончания типа .[0-9$]
#         if re.search('\.[0-9]$', items[item]): 
#             items[item] = items[item][:-2]
#         items[item] = items[item][:64]                                                                          # Обрезаем имя столбца до 64 символов
#     question.columns = items
#     # Устанавливаем наличие ответов как 1, отсутствие - 0
#     question = (question.replace('.*',1,regex=True))
#     question = (question.fillna(0))
#     question = (question.astype(int))
#     # Склеиваем с логинами
#     frames = pd.concat([logins,question], axis=1).drop(index=[0])
#     # Кладём в бд, или ложим, или складываем, или слаживаем, пох
#     frames.to_sql(tablename,con=engine,if_exists='replace')
#     pass

# def InsertSingleAnswerQueIntoDB(question_coords, tablename):
#     single_answer_question = (pd.read_excel(input_file, usecols=question_coords, header=2,skiprows=0,names=['answer']))
#     result_table = pd.concat([logins,single_answer_question], axis=1).drop(index=[0])
#     result_table.to_sql(tablename,con=engine,if_exists='replace')
    
# for question in column_question:
#     table_name = table_name_example + str(question[1])
#     InsertQuestionIntoDB(question[0],table_name)
#     print(table_name,' импортирована.')

# for question in column_questions_one_answer:
#     table_name = table_name_example + str(question[1])
#     InsertSingleAnswerQueIntoDB(question[0],table_name)
#     print(table_name,' импортирована.')

# rpg_style_questions = (pd.read_excel(input_file, usecols=column_questions_answer_rpg_style[0], header=2,skiprows=0))
# rpg_style_questions = (rpg_style_questions.fillna(0).astype(int))
# rpg_stype_table = pd.concat([logins,rpg_style_questions], axis=1).drop(index=[0])
# rpg_stype_table_name = table_name_example + str(column_questions_answer_rpg_style[1])
# rpg_stype_table.to_sql(rpg_stype_table_name,con=engine,if_exists='replace')
# print (chief_logins,'\n',stuff_logins)