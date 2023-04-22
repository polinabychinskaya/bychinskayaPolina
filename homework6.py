import datetime
import time
import os
from colorama import init
init()
from colorama import Fore, Back, Style


nums = [
'''
    ■■■■■
  ■■■   ■■■
  ■■     ■■
  ■■■   ■■■
    ■■■■■''',
'''
     ■■■
   ■■■■■
     ■■■
     ■■■
     ■■■''',
'''
   ■■■■■■■
        ■■
     ■■■
   ■■    
   ■■■■■■■''',
'''
   ■■■■■■■
       ■■■
     ■■■■■
       ■■■
   ■■■■■■■''',
 '''
   ■■   ■■
   ■■   ■■
   ■■■■■■■
        ■■
        ■■''',
 '''
   ■■■■■■■
   ■■
   ■■■■■■
        ■■
   ■■■■■■''',
 '''
   ■■■■■■■
   ■■    
   ■■■■■■
   ■■   ■■
    ■■■■■''',
 '''
   ■■■■■■■■
         ■■
       ■■
     ■■
     ■■''',
 '''
    ■■■■■
   ■■   ■■
     ■■■
   ■■   ■■
    ■■■■■''',
 '''
    ■■■■■
   ■■   ■■
     ■■■■■
        ■■
   ■■■■■■■''',
 '''
    ■  
    ■  


    ■  
    ■  
'''
]


while True:
    nums_by_column = [s.split('\n') for s in nums]
    nums_by_line = zip(*nums_by_column)
    max_length_by_column = [
        max([len(s) for s in col_nums])
        for col_nums in nums_by_column
    ]
    clock_time = datetime.datetime.now()
    time_now = clock_time.strftime("%H:%M:%S")
    time_split = [int(t) for t in time_now if t != ":"]
    for parts in nums_by_line:
        padded_strings = [
            parts[i].ljust(max_length_by_column[i])
            for i in range(len(parts))
        ]
        print(Fore.GREEN + ''.join(padded_strings[time_split[0]]) + ''.join(padded_strings[time_split[1]]) + ''.join(padded_strings[10]) + ''.join(padded_strings[time_split[2]]) + ''.join(padded_strings[time_split[3]]) + ''.join(padded_strings[10]) + ''.join(padded_strings[time_split[4]]) + ''.join(padded_strings[time_split[5]]))
    time.sleep(1)
    os.system('cls')
