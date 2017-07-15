import pandas as pd
import numpy as np
import sys
import time
import datetime
import argparse
from pprint import pprint


def check_the_table(path):

    table = pd.read_excel(path)
    errors = []
    check_contract_time(table,errors)
    #check_room_area(table,errors)
    check_gender_in_room(table,errors)
    return errors


def check_contract_time(table,errors):

    present = datetime.datetime.now()
    for index,date in enumerate(table['date_stop']):
        if (not pd.isnull(date)) and (present > date):
            errors.append('Room {num}:row#{row} expired'.format(num=table['Number'][index],row=index))

def check_room_area(table,errors):#Havent enought information in table, doesnt work

    pers_room = table.copy()

    for index  in pers_room['person_full_name'].index:
        if not pd.isnull(pers_room['person_full_name'][index]):
            pers_room.set_value(index,'person_full_name',1)
        else:
            pers_room.set_value(index,'person_full_name',0)

    for index,room  in enumerate(table['Number']):
        if not (pers_room.loc[pers_room['Number'] == room,'person_full_name'].sum()) < ((1/6)*19):
            errors.append('room {num}:row#{row} less than 6m^2 on one citizen '.format(num=room,row=index))

def check_gender_in_room(table,errors):

    pers_room = table.copy()
    pers_room['gender'].replace(to_replace=['m', 'f'],value=[-1,1],inplace=True)

    for index,room  in enumerate(table['Number']):
        temp=pers_room.loc[pers_room['Number'] == room,['Number','gender']]
        if  abs(temp['gender'].sum()) != temp['Number'].size:
            errors.append('room {num}:row#{row} gender'.format(num=room,row=index))



if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Check xlsx tables',epilog="!!Support only excel!!")
    parser.add_argument ('file',help='Path to  table for checking')
    namespace = parser.parse_args()
    pprint(check_the_table(namespace.file))
