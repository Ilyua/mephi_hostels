import xlrd
import argparse
from pprint import pprint


def __printProgressBar (iteration, total, prefix = 'Progress:', suffix = 'Complete',  decimals = 1, length = 50, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

def comparison(path_1,path_2):

    book_1 = xlrd.open_workbook(path_1)
    sheet_1 = book_1.sheet_by_index(0)

    book_2 = xlrd.open_workbook(path_2)
    sheet_2 = book_2.sheet_by_index(0)

    errors = []
    if sheet_1.nrows != sheet_2.nrows or sheet_1.ncols != sheet_2.ncols:
        sys.exit('Unsuitable files for comparison')
    else:
        rows = sheet_1.nrows
        columns =  sheet_1.ncols
        l = rows*columns
        i = 0
        __printProgressBar(i, l)
        for row in range(rows):
            for col in range(columns):
                data_1 = sheet_1.cell_value(row,col)
                data_2 = sheet_2.cell_value(row,col)
                if data_1 != data_2:
                    errors.append({'position': (row,col),
                                    'in {}'.format(path_1):data_1,
                                    'in {}'.format(path_2):data_2})
                i+=1
                __printProgressBar(i, l)
    return errors

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Comparison two xlsx tables', epilog="!!Support only excel!!")
    parser.add_argument ('file1', help='Path to first table for comparison')
    parser.add_argument ('file2', help='Path to second table for comparison')
    namespace = parser.parse_args()
    pprint(comparison(namespace.file1,namespace.file2))








