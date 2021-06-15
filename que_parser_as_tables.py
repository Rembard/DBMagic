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
stuff_logins = (pd.read_excel(input_file_stuff, usecols=column_logins_stuff,header=2, skiprows=0,names=['logins']))          #Получаем логины
chief_logins = (pd.read_excel(input_file_chief, usecols=column_logins_chief,header=2, skiprows=0,names=['logins']))          #Получаем логины
# dop_link = (pd.read_excel(input_file, usecols='E',header=2, skiprows=0,names=['Источник ответа']))
# dop_link['Источник ответа'] = dop_link['Источник ответа'].str[13:]
# logins = pd.concat([logins,dop_link],axis=1)
# print (logins)

def MergeChiefLogins():
    chief_logins = (pd.read_excel(input_file_chief, usecols=column_logins_chief,header=2, skiprows=0,names=['logins']))             #Получаем логины
    dop_link = (pd.read_excel(input_file_chief, usecols=column_chief_dop_link,header=2, skiprows=0,names=['Источник ответа']))
    dop_link['Источник ответа'] = dop_link['Источник ответа'].str[13:]
    chief_logins = pd.concat([chief_logins,dop_link],axis=1)
    return chief_logins

#chief_logins = MergeChiefLogins()

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

# InsertChiefRpgStyleQueIntoDB()
# InsertChiefQuestionIntoDB()
# InsertChiefSingleAnswerQueIntoDB()
# InsertStuffRpgStyleQueIntoDB()
# InsertStuffQuestionIntoDB()
# InsertStuffSingleAnswerQueIntoDB()



#all_chief_questtions = sorted(all_chief_questtions, key=itemgetter(1))
# for question in all_chief_questtions:

#testframe = pd.read_excel(input_file_chief, usecols='P:AI', header=2, skiprows=0)
#testframe2 = pd.read_excel(input_file_chief, usecols='AJ:BK', header=2, skiprows=0)
#testframe = QuestionSlice(input_file_chief, 'P:AI', 2, 0).concatcolumns()
#testframe = testframe.concatcolumns()

emptyarray = []
questionname = []
for i in all_chief_questtions:                                                                                          #Перебор столбцов для формирования таблички concat_table
    question = QuestionSlice(input_file_chief, i[0],2,0)
    questionname.append('Question'+str(i[1]))                                                                           #Создаём имя столбца
    if i[1] in (11,16,21,41,43,44,45):
        question = question.createanswer()
        emptyarray.append(question)
    elif i[1] == 23:
        question = question.createrpganswer()
        # Попытка сделать сортировку через списки
        for header in question.columns:
            for index in question.index:
                question.loc[index,[header]] = f'{question.loc[index,[header]].values[0]} - {header}'
        # data_list = question.values.tolist()
        # for data in data_list:
        #     data.sort(key= lambda x:str(x)[0])
        # empty_frame = pd.DataFrame({'Question23': data_list}, index=None)
        ############################################################################################
        #question = pd.concat([chief_logins, question], axis=1).drop(index=[0])
        question = question.T
        print (question)
        #emptyarray.append(empty_frame)

        #empty_frame.astype(str).to_sql('blablabla',con=engine,if_exists='replace')
        #emptyarray.append(empty_frame)
        #print(empty_frame)
        # b = (question.values.tolist())
        # b = sorted(b, key=itemgetter(2))
        #print (b)
        #print (question.values.tolist()).sorted(key=itemgetter(2))
        #empty_frame = pd.DataFrame({'Nazvanie_stolba': question.values.tolist()})
        #empty_frame['Nazvanie_stolba'].apply(sorted)
        #empty_frame['Nazvanie_stolba'].apply(lambda object: sorted(object, key = lambda cell_value: cell_value[0]))
        #print(empty_frame)

        #emptyarray.append(question)
    else:
        question = question.concatcolumns()
        emptyarray.append(question)
#result = pd.concat(emptyarray, axis=1)
#result.columns = (questionname)
#result.to_sql('testresult', con=engine,if_exists='replace')
#print (result)
