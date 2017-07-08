import pandas as pd
import numpy
import sys
from pprint import pprint
import time
import xlrd

def check_the_table(path_1):

    table_1 = pd.read_excel(path_1)


    Errors = []

    for key in table_1.keys():
    #key = 'Номер комнаты'
        for index in range(table_1[key].size):
            data_1=table_1[key][index]

            if not check_value(key,data_1):
                # pprint({'position': (key,index),
                #                'data_1':data_1})
                Errors.append({'position': (key,index),
                               'data_1':data_1})
    return Errors

def check_value(column_name, cell_value):#column_name_function
    # if pd.isnull(cell_value):
    #     return True
    if 'Адрес корпуса общежития' in column_name:
        return is_string(cell_value)
    elif 'Этаж' in column_name:
        return is_int(cell_value)
    elif 'Номер комнаты' in column_name:
        return is_int(cell_value)
    elif 'Кол-во койкомест' in column_name:
        return is_int(cell_value)
    elif 'Площадь комнаты' in column_name:
        print(type(cell_value))
        return is_float(cell_value)
    elif 'ФИО' in column_name:
        return is_string(cell_value)
    elif 'Номер дог' in column_name:
        return True
    elif 'Сроки договора' in column_name:
        return True
    elif 'Категория проживающего' in column_name:
        return is_string(cell_value)
    elif 'Unnamed' in column_name:
        return is_string(cell_value)
    else:
        print('Not found',column_name)










# def belonging(value):
#     return (value in ['общежитие'])


def is_string(value):

    try:
        str(value)
        return True
    except:
        return False

def is_float(value):
    return isinstance(value, numpy.float64)


def is_int(value):
    try:
        int(value)
        return True
    except:
        return False

#table_1 = pd.read_excel('./hostels.xlsx')
pprint(check_the_table('./checking_table.xlsx'))

