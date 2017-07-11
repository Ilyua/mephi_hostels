import pandas as pd
import numpy as np
import sys
from pprint import pprint
import time
import xlrd


def comparison_xlrd(path_1,path_2):

    book_1 = xlrd.open_workbook(path_1)
    sheet_1 = book_1.sheet_by_index(0)

    book_2 = xlrd.open_workbook(path_2)
    sheet_2 = book_2.sheet_by_index(0)

    Errors = []
    if sheet_1.nrows != sheet_2.nrows or sheet_1.ncols != sheet_2.ncols:
        sys.exit('Unsuitable files for comparison')
    else:
        rows = sheet_1.nrows
        columns =  sheet_1.ncols

        for row in range(rows):
            for col in range(columns):
                data_1 = sheet_1.cell_value(row,col)
                data_2 = sheet_2.cell_value(row,col)
                if data_1 != data_2:
                    Errors.append({'position': (row,col),
                                    'data_1':data_1,
                                    'data_2':data_2})
    return Errors

if __name__=='__main__':
    def comparison_pandas(path_1,path_2):

        table_1 = pd.read_excel(path_1, na_values=['NA'])
        table_2 = pd.read_excel(path_2, na_values=['NA'])

        Errors = []

        if len(table_1.keys())!= len(table_2.keys()):
                sys.exit('Unsuitable files for comparison')

        comp = table_1 == table_2
        comp_m=comp.as_matrix()
        print(np.where(comp == False))

        for key in comp.keys():
            for index in range(comp[key].size):
                if not comp[key][index]:
                    Errors.append((key,index))
        return Errors

    def time_decorator(function):
        def timer(path_1,path_2):
            start = time.time()
            err = function(path_1,path_2)
            stop = time.time()
            sec = stop - start
            print(sec)
            return err
        return timer

    dec_comp_xlrd = time_decorator(comparison_xlrd)
    dec_comp_pandas = time_decorator(comparison_pandas)

    print('Без pandas:')
    pprint(dec_comp_xlrd('./hostels.xlsx', './hostels1.xlsx'))
    print('С pandas:')
    pprint(dec_comp_pandas('./hostels.xlsx', './hostels1.xlsx'))
