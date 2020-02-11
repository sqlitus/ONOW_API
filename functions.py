import pandas as pd
import numpy as np
import glob
import os
from datetime import datetime
import sys


# Function to import & append (SQL Union) excel or CSV
def import_merge_clean(files, filetype='excel', start_col='Start', end_col='End', value_col='Value', id_col='Number'):
    '''
    import all files, filter out flash assigns & redundant assigns.

    :param files:
    :param filetype:
    :param start_col:
    :param end_col:
    :param value_col:
    :param id_col:
    :return:
    '''

    if filetype == 'csv':  # encoding ISO-8859-1 seems to work more than latin1.
        df = pd.concat((pd.read_csv(file, encoding='ISO-8859-1') for file in files), ignore_index=True).drop_duplicates()
    else:
        df = pd.concat((pd.read_excel(file) for file in files), ignore_index=True).drop_duplicates()


    # FILTER OUT: flash assignments. (Exclude Start == End records via anti-join (Keep in A not in B))
    filter_out = df[df[start_col] == df[end_col]].copy()  # copy of values, not ref
    df = df.merge(filter_out, how='left', indicator=True)
    df = df[df['_merge'] == 'left_only'].drop(columns='_merge')


    # FILTER OUT: redundant re-assignments. (assignment to same entity as previous assignment)
    df = df.sort_values([id_col, start_col])  # sort for window functions to work
    df['prev_team'] = df.groupby(id_col)[value_col].shift(1)
    filter_out_redundant_assignments = df[df[value_col] == df['prev_team']]
    df = df.merge(filter_out_redundant_assignments, how='outer',indicator=True).query('_merge == "left_only"').drop(columns=['_merge', 'prev_team'])

    print('Import, merge, clean successful')
    print(f'Rows: {df.shape[0]}')
    print(f'data size: {assignment_group_history.__sizeof__() / 1048576} MBs')

    return df




class Benchmarking:
    """object for benchmarking script run time"""


    start_time = datetime.now()
    start_time_formatted = start_time.strftime('%m/%d/%y %H:%M:%S %p')
    prev_time = None  # instantiates w/ none
    print('Start time:', start_time_formatted)
    elapsed_total = 0  # test for accessing prop

    def elapsed(self, message='', end='no', prev_time=prev_time, start_time=start_time, start_time_formatted=start_time_formatted):


        now = datetime.now()


        # CALC: elapsed between prev run and now
        if prev_time is None:
            elapsed_time = round((now - self.start_time).total_seconds())
            print(f'Time since benchmarking start: {elapsed_time} sec')
        else:
            elapsed_time = round((now - self.prev_time).total_seconds())
            print(f'Time since last benchmark: {elapsed_time} sec')
        self.elapsed_total = round((now - self.start_time).total_seconds())

        if message != '':
            print(message)

        if end == 'yes':
            print('DONE.\nStart time: ', start_time_formatted,
                  '\n', 'Current time: ', now.strftime('%m/%d %H:%M:%S %p'),
                  '\n', 'Total elapsed time: ', self.elapsed_total, ' seconds', sep='')

        self.prev_time = now

# # usage
# x = Benchmarking()
# x.start_time
# x.start_time_formatted
# x.elapsed()
# x.elapsed('DONE.')



# finding files
def show_filepaths(path_rawstring = "", file_wildcard_pattern = '*'):
    if path_rawstring == "":
        path = os.getcwd()

    # glob.glob('*')  # files in current directory
    return glob.glob(path + '/' + file_wildcard_pattern) # basic wildcard matching

# show_filepaths()