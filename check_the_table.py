import pandas as pd
import numpy as np
import sys
from pprint import pprint
import time
import xlrd

def check_the_table(path_1):

    table_1 = pd.read_excel(path_1)

    Errors = []

    for key in table_1.keys():

        for index in range(table_1[key].size):
            data_1=table_1[key][index]

            if not check_value(key,data_1):

                Errors.append({'position': (key,index),
                               'data_1':data_1})
    return Errors

def check_value(column_name, cell_value):#column_name_function
    # if pd.isnull(cell_value):
    #     return True
    if 'Адрес корпуса общежития' in column_name:
        return check_address_of_hostel(cell_value)
    elif 'Этаж' in column_name:
        return check_floorcheck(cell_value)
    elif 'Номер комнаты' in column_name:
        return check_room_number(cell_value)
    elif 'Кол-во койкомест' in column_name:
        return check_places_amount(cell_value)
    elif 'Площадь комнаты' in column_name:
        return check_room_square(cell_value)
    elif 'ФИО' in column_name:
        return check_first_last_name(cell_value)
    elif 'Номер дог' in column_name:
        return check_contract_number(cell_value)
    elif 'Сроки договора' in column_name:
        return check_contract_time(cell_value)
    elif 'Категория проживающего' in column_name:
        return check_resident_category(cell_value)
    elif 'Unnamed' in column_name:
        return True
    else:
        print('Not found',column_name)



def check_address_of_hostel(cell_value):
    return isinstance(cell_value,str)

def check_floorcheck(cell_value):
    return isinstance(cell_value,np.int64)

def check_room_number(cell_value):
    return isinstance(cell_value,np.int64)

def check_places_amount(cell_value):

    return isinstance(cell_value,np.float64) and  ( not np.isnan(cell_value) )

def check_room_square(cell_value):
    return isinstance(cell_value,np.float64)

def check_first_last_name(cell_value):
    return isinstance(cell_value,str)

def check_contract_number(cell_value):
    return True

def check_contract_time(cell_value):
    return True

def check_resident_category(cell_value):
    return isinstance(cell_value,str) or isinstance(cell_value,float)










def is_string(cell_value):

    try:
        str(cell_value)
        return True
    except:
        return False

def is_float(cell_value):
    return isinstance(cell_value, numpy.float64)


def is_int(cell_value):
    try:
        int(cell_value)
        return True
    except:
        return False

#table_1 = pd.read_excel('./hostels.xlsx')
pprint(check_the_table('./checking_table.xlsx'))

