from numpy.lib.arraypad import pad
import pandas as pd
import re
# from file_to_parse import *

# file = "C:\\Users\\artur.rakhmanov\\Projects\\DBMagic\\Результаты_все_сотрудники.xlsx"
class QuestionSlice():

    def __init__(self, file, columns, header,skiprows):
        self.file = file
        self.columns = columns
        self.header = header
        self.skiprows = skiprows
        self.filebody = pd.read_excel(self.file, usecols=self.columns, header=self.header, skiprows=self.skiprows)
        
    
    def transquetobin(self):
        """Конкатит одинаковые столбцы, меняет ответы на бинарные, обрезает нумерацию столбцов от pandas"""
        column_names = self.filebody.columns.values.tolist()
        for i in range(len(column_names)):
            target_column = column_names[i]
            for column in column_names:
                if target_column.upper() == column[:-2].upper():
                    self.filebody[target_column] = self.filebody[target_column].combine_first(self.filebody[column])
                    del self.filebody[column]
        # Удаляем лишние символы в заголовках столбцов
        column_names = self.filebody.columns.values.tolist()                                 # Обновляем массив, так как могли быть удалены столбцы
        for column in range(len(column_names)):                                              # Проверка по регулярке на окончания типа .[0-9$]
            if re.search('\.[\d]$', column_names[column]):
                column_names[column] = column_names[column][:-2]
            column_names[column] = column_names[column][:64]                                 # Обрезаем имя столбца до 64 символов
        self.filebody.columns = column_names
        # Устанавливаем наличие ответов как 1, отсутствие - 0
        self.filebody = (self.filebody.replace('.*',1,regex=True))
        self.filebody = (self.filebody.fillna(0))
        self.filebody = (self.filebody.astype(int))
        return self.filebody

    def createanswer(self):
        """Возвращает датафрейм с ответами"""
        self.filebody.columns = ['answer']
        return self.filebody

    def createrpganswer(self):
        """Возвращает датафрейм с ответами, преобразовав в Int"""
        self.filebody = (self.filebody.fillna(0).astype(int))
        return self.filebody

    def concatcolumns(self):
        for header in self.filebody.columns:
            self.filebody.loc[self.filebody[header].notna(), header] = header
        self.filebody = self.filebody.astype('str').replace("nan",'')
        self.filebody = self.filebody.apply(lambda object: '\n'.join(list(filter(lambda a: a != '', object))), axis=1)
        return self.filebody
    # def mergechieflogins(self):
    #     """Объединяет столбцец логинов со столбцом Источник ответа"""
    #     dop_link = (pd.read_excel(input_file_chief, usecols='E',header=2, skiprows=0,names=['Источник ответа']))
    #     dop_link['Источник ответа'] = dop_link['Источник ответа'].str[13:]
    #     self.filebody = pd.concat([self.filebody,dop_link],axis=1)
    #     return self.filebody