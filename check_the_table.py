import pandas as pd
import sys
from pprint import pprint
import time
import xlrd

def check_the_table(path_1):

    table_1 = pd.read_excel(path_1)


    Errors = []

    #for key in table_1.keys():
    key = 'Номер комнаты'
    for index in range(table_1[key].size):
        data_1=table_1[key][index]

        if not check_value(key,data_1):
            Errors.append({'position': (key,index),
                           'data_1':data_1})
    return Errors

def check_value(column_name, cell_value):#column_name_function
    if column_name == 'Принадлежность':
        return belonging(cell_value)
    elif column_name == 'Номер комнаты':
        return room_number(cell_value)

def belonging(value):
    return (value in ['общежитие'])
def room_number(value):
    try:
        int(value)
        return True
    except:
        return False

#table_1 = pd.read_excel('./hostels.xlsx')
pprint(check_the_table('./hostels.xlsx'))

