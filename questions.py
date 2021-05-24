import MySQLdb
import pandas as pd
connection_params_sql = {'host': '10.144.198.132',
                         'user': "mon_report_bti",
                         'passwd': "Report_112233",
                         'charset': "utf8",
                         'db': "test"}

# Читаем файл
input_file = pd.read_excel('Опросник.xlsx')
logins = input_file['Логин'].values.tolist()
answers = input_file['Страница 2'].values.tolist()

# Убираем первые три строки, так как они не используются
answers = answers[3:]
logins = logins[3:]

# Группируем юзеров и их ответы
login_answers = list(zip(logins,answers))

# Удаляем пустые строки и получаем массив со столбцами ответов
answers_clean = []
for i in range(len(answers)):
    if not pd.isna(answers[i]):
        answers_clean.append(answers[i])

#Удаляем юзеров без ответов
import_data = []
for b in range(len(login_answers)):
    if not pd.isna(login_answers[b][1]):
        import_data.append(login_answers[b])

# Создаем подключение
con_serv = MySQLdb.connect(**connection_params_sql)
# устанавливаем курсор
cur_serv = con_serv.cursor()
# Создаем таблицу
create_query = ("""CREATE TABLE IF NOT EXISTS `test`.`Anketa.Question6` (id Int NOT NULL PRIMARY KEY AUTO_INCREMENT, logins VARCHAR (120), """)
for i in range(len(answers_clean)):
    create_query+=answers_clean[i]
    create_query+=' INT DEFAULT 0, '
create_query = (create_query[0:-2])
create_query +=');'
print (create_query)
cur_serv._query(create_query)
# Вставляем содержимое
for n in range(len(import_data)):
    todb_insert_query = (f'INSERT INTO `Anketa.Question6`(logins,{import_data[n][1]}) VALUES (\'{import_data[n][0]}\', 1);')
    print (todb_insert_query)
    cur_serv.execute(todb_insert_query)

# #Закрываем соединение
cur_serv.close()
con_serv.commit()
con_serv.close()