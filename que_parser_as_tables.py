from numpy import NaN, column_stack, empty, inner, nan
import numpy as np
import pandas as pd
import re
from operator import itemgetter
from pymysql import NULL
from classes import *
from file_to_parse import *
from sqlalchemy import create_engine
from connection_params import db_creds,db_charset

engine = create_engine(db_creds,encoding=db_charset)
stuff_logins = (pd.read_excel(input_file_stuff, usecols=column_logins_stuff,header=2, skiprows=0,names=['logins']))      #Получаем логины
chief_logins = (pd.read_excel(input_file_chief, usecols=column_logins_chief,header=2, skiprows=0,names=['logins']))      #Получаем логины
logins_concat_leftside_chief = (pd.read_excel(input_file_chief, usecols='A:C,G:H,J:O',header=2, skiprows=0, names=['id_answer', 'date_answer', 'time_answer', 'IP_hash', 'UA_hash','Login', 'FIO', 'Email', 'MRF', 'Region', 'Number']))
logins_concat_leftside_stuff = (pd.read_excel(input_file_stuff, usecols='A:C,G:N',header=2, skiprows=0, names=['id_answer', 'date_answer', 'time_answer', 'IP_hash', 'UA_hash','Login', 'FIO', 'Email', 'MRF', 'Region', 'Number']))
all_chief_questions = sorted(all_chief_questions, key=itemgetter(1))                                                     #Сортируем массив всех вопросов чифа
all_stuff_questions = sorted(all_stuff_questions, key=itemgetter(1))                                                     #Сортируем массив всех вопросов стаффа


def MergeChiefLogins():
    chief_logins = (pd.read_excel(input_file_chief, usecols=column_logins_chief,header=2, skiprows=0,names=['logins']))  #Получаем логины
    dop_link = (pd.read_excel(input_file_chief, usecols=column_chief_dop_link,header=2, skiprows=0,names=['Источник ответа']))
    dop_link['Источник ответа'] = dop_link['Источник ответа'].str[13:]
    chief_logins = pd.concat([chief_logins,dop_link],axis=1)
    return chief_logins

chief_logins = MergeChiefLogins()

def InsertChiefQuestionIntoDB():
    for question in column_question_chief:
        obj_question = QuestionSlice(input_file_chief,question[0], 2 ,0)
        obj_question = pd.concat([chief_logins,obj_question.transquetobin()], axis=1).drop(index=[0])
        table_name = table_name_chief_example+str(question[1])
        obj_question.to_sql(table_name,con=engine,if_exists='replace')
        print (table_name,' импортирована')

def InsertChiefSingleAnswerQueIntoDB():
    for question in column_question_chiefs_one_answer:
        obj_question = QuestionSlice(input_file_chief,question[0], 2 ,0)
        obj_question = pd.concat([chief_logins,obj_question.createanswer()], axis=1).drop(index=[0])
        table_name = table_name_chief_example+str(question[1])
        obj_question.to_sql(table_name,con=engine,if_exists='replace')
        print (table_name, ' импортирована')

def InsertChiefRpgStyleQueIntoDB():
    for question in column_question_chiefs_answer_rpg_style:
        obj_queston = QuestionSlice(input_file_chief,question[0], 2, 0)
        obj_queston = pd.concat([chief_logins,obj_queston.createrpganswer()], axis=1).drop(index=[0])
        table_name = table_name_chief_example+str(question[1])
        obj_queston.to_sql(table_name,con=engine,if_exists='replace')
        print (table_name, ' импортирована')

#stuff

def InsertStuffQuestionIntoDB():
    for question in column_question_stuff:
        obj_question = QuestionSlice(input_file_stuff,question[0], 2 ,0)
        obj_question = pd.concat([stuff_logins,obj_question.transquetobin()], axis=1).drop(index=[0])
        table_name = table_name_stuff_example+str(question[1])
        obj_question.to_sql(table_name,con=engine,if_exists='replace')
        print (table_name,' импортирована')

def InsertStuffSingleAnswerQueIntoDB():
    for question in column_question_stuff_one_answer:
        obj_question = QuestionSlice(input_file_stuff,question[0], 2 ,0)
        obj_question = pd.concat([stuff_logins,obj_question.createanswer()], axis=1).drop(index=[0])
        table_name = table_name_stuff_example+str(question[1])
        obj_question.to_sql(table_name,con=engine,if_exists='replace')
        print (table_name, ' импортирована')

def InsertStuffRpgStyleQueIntoDB():
    for question in column_question_stuff_answer_rpg_style:
        obj_queston = QuestionSlice(input_file_stuff,question[0], 2, 0)
        obj_queston = pd.concat([stuff_logins,obj_queston.createrpganswer()], axis=1).drop(index=[0])
        table_name = table_name_stuff_example+str(question[1])
        obj_queston.to_sql(table_name,con=engine,if_exists='replace')
        print (table_name, ' импортирована')

def InsertContatChiefTable():
    chief_contat_questions = []
    chief_concat_columns = []
    for i in all_chief_questions:                                                                                          #Перебор столбцов для формирования таблички concat_table
        question = QuestionSlice(input_file_chief, i[0],2,0)
        chief_concat_columns.append('Question'+str(i[1]))                                                                           #Создаём имя столбца
        if i[1] in (11,16,21,41,43,44,45):
            question = question.createanswer()
            chief_contat_questions.append(question)
        elif i[1] == 23:
            question = question.sortrpganswer()
            chief_contat_questions.append(question)
        else:
            question = question.concatcolumns()
            chief_contat_questions.append(question)
    chief_contat_questions = pd.concat(chief_contat_questions,axis=1)
    chief_contat_questions.columns = (chief_concat_columns)
    chief_contat_questions = pd.concat([logins_concat_leftside_chief,chief_contat_questions],axis=1).drop(index=[0])
    chief_contat_questions.to_sql('questioning.chief.concat_table', con=engine,if_exists='replace')

def InsertContatStuffTable():
    stuff_contat_questions = []
    stuff_concat_columns = []
    for i in all_stuff_questions:                                                                                        #Перебор столбцов для формирования таблички concat_table
        question = QuestionSlice(input_file_stuff, i[0],2,0)
        stuff_concat_columns.append('Question'+str(i[1]))                                                                           #Создаём имя столбца
        if i[1] in (10,15,20,40,42,44,45,46,47,48,50,51):
            question = question.createanswer()
            stuff_contat_questions.append(question)
        elif i[1] == 22:
            question = question.sortrpganswer()
            stuff_contat_questions.append(question)
        else:
            question = question.concatcolumns()
            stuff_contat_questions.append(question)
    stuff_contat_questions = pd.concat(stuff_contat_questions,axis=1)
    stuff_contat_questions.columns = (stuff_concat_columns)
    stuff_contat_questions = pd.concat([logins_concat_leftside_stuff,stuff_contat_questions],axis=1).drop(index=[0])
    stuff_contat_questions.to_sql('questioning.stuff.concat_table', con=engine,if_exists='replace')

# InsertChiefRpgStyleQueIntoDB()
# InsertChiefQuestionIntoDB()
# InsertChiefSingleAnswerQueIntoDB()
# InsertStuffRpgStyleQueIntoDB()
# InsertStuffQuestionIntoDB()
# InsertStuffSingleAnswerQueIntoDB()
InsertContatChiefTable()
InsertContatStuffTable()


