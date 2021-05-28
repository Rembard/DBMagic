input_file = "C:\\Users\\artur.rakhmanov\\Projects\\DBMagic\\Результаты_руководители.xlsx"

#DB name table vars
table_name_example = 'Anketa.Question.Boss'
first_table_number = 6                                                                                      #С какого номера именовать таблицы

# File structure Результаты_руководители
column_logins = 'L'                                                                                         #Столбец логинов
column_question = []
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

# File parse Результаты_все_сотрудники
# column_logins = 'I'                                                                                         #Столбец логинов
# column_question = []
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