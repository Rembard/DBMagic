import numpy as np
import pandas as pd

# import xlrd
# import openpyxl

from sqlalchemy import create_engine, engine

engine = create_engine('mysql://mon_report_bti:Report_112233@10.144.198.132/test?charset=utf8mb4')
df = pd.read_excel('Опросник.xlsx', usecols="I,N")
df.to_sql('Anketa_Question6', con=engine)
























# path = "C:\\Users\\artur.rakhmanov\\Projects\\DBMagic\\try_to_import.xlsx"
# wb_obj = openpyxl.load_workbook(path)
# sheet_obj = wb_obj.active
# max_col = sheet_obj.max_column
# max_row = sheet_obj.max_row

# print(sheet_obj, max_col, max_row)


# df = pd.DataFrame({'Name': ['Manchester City', 'Real Madrid', 'Liverpool',
#                             'FC Bayern München', 'FC Barcelona', 'Juventus'],
#                    'League': ['English Premier League (1)', 'Spain Primera Division (1)',
#                               'English Premier League (1)', 'German 1. Bundesliga (1)',
#                               'Spain Primera Division (1)', 'Italian Serie A (1)'],
#                    'TransferBudget': [176000000, 188500000, 90000000,
#                                       100000000, 180500000, 105000000]})


# df.to_excel('./teams.xlsx', sheet_name='Budgets', index=False)

















# slovar = {'Name':'Рустам','Fathername':'Каримович','Soname':'Гмыря','Age':1}
# arr = np.array(slovar)
# arr2 = np.array([1,2,3,4,5])
# print(arr.dtype, '\n', arr.size)