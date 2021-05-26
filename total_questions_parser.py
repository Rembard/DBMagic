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

input_columns_que6 = pd.read_excel(input_file, usecols="O:AH", nrows=1 ,skiprows=1)
input_columns_que7 = pd.read_excel(input_file, usecols="AI:BJ", nrows=1 ,skiprows=1)
input_columns_que8 = pd.read_excel(input_file, usecols="BK:BT", nrows=1 ,skiprows=1)
input_columns_que9 = pd.read_excel(input_file, usecols="BV:CO", nrows=1 ,skiprows=1)
input_columns_que10 = pd.read_excel(input_file, usecols="CP:DQ", nrows=1 ,skiprows=1)
input_columns_que11 = pd.read_excel(input_file, usecols="DR:EA", nrows=1 ,skiprows=1)
input_columns_que12 = pd.read_excel(input_file, usecols="EC:EV", nrows=1 ,skiprows=1)
input_columns_que13 = pd.read_excel(input_file, usecols="EW:FX", nrows=1 ,skiprows=1)
input_columns_que14 = pd.read_excel(input_file, usecols="FY:GF", nrows=1 ,skiprows=1)
input_columns_que15 = pd.read_excel(input_file, usecols="GJ:HK", nrows=1 ,skiprows=1)
input_columns_que16 = pd.read_excel(input_file, usecols="HL:HS", nrows=1 ,skiprows=1)
input_columns_que17 = pd.read_excel(input_file, usecols="HT:JX", nrows=1 ,skiprows=1)
input_columns_que18 = pd.read_excel(input_file, usecols="JY:LD", nrows=1 ,skiprows=1)
input_columns_que19 = pd.read_excel(input_file, usecols="LE:MI", nrows=1 ,skiprows=1)
input_columns_que20 = pd.read_excel(input_file, usecols="MJ:OQ", nrows=1 ,skiprows=1)
input_columns_que21 = pd.read_excel(input_file, usecols="OR:PO", nrows=1 ,skiprows=1)
input_columns_que22 = pd.read_excel(input_file, usecols="PP:RH", nrows=1 ,skiprows=1)
input_columns_que23 = pd.read_excel(input_file, usecols="AI:BJ", nrows=1 ,skiprows=1)
input_columns_que24 = pd.read_excel(input_file, usecols="RI:SY", nrows=1 ,skiprows=1)
input_columns_que25 = pd.read_excel(input_file, usecols="SZ:UE", nrows=1 ,skiprows=1)
input_columns_que26 = pd.read_excel(input_file, usecols="UF:VI", nrows=1 ,skiprows=1)
input_columns_que27 = pd.read_excel(input_file, usecols="VJ:WM", nrows=1 ,skiprows=1)
input_columns_que28 = pd.read_excel(input_file, usecols="WN:XW", nrows=1 ,skiprows=1)
input_columns_que29 = pd.read_excel(input_file, usecols="XX:ZY", nrows=1 ,skiprows=1)
input_columns_que30 = pd.read_excel(input_file, usecols="ZZ:ABG", nrows=1 ,skiprows=1)
input_columns_que31 = pd.read_excel(input_file, usecols="ABH:ACL", nrows=1 ,skiprows=1)
input_columns_que32 = pd.read_excel(input_file, usecols="ACM:ADX", nrows=1 ,skiprows=1)
input_columns_que33 = pd.read_excel(input_file, usecols="ADZ:AER", nrows=1 ,skiprows=1)
input_columns_que34 = pd.read_excel(input_file, usecols="AET:AEX", nrows=1 ,skiprows=1)
input_columns_que35 = pd.read_excel(input_file, usecols="AEZ:AFA", nrows=1 ,skiprows=1)
table_columns = input_columns_que12.values.tolist()
print (table_columns)

# Приводим в порядок заголовки
# def parse_columns(raw_columns):
#     table_columns = input_columns.values.tolist()
#     table_columns = str(table_columns).strip("""[']""")
#     table_columns = table_columns.split("""', '""")
#     return table_columns
# columns_question_6 = parse_columns(input_columns)
# print (columns_question_6)