import os
import sys
from Athlete import Athlete

#列印清單
def print_list(the_list,indent = False, level=0):
    for eachItem in the_list:
        if(isinstance(eachItem, list)):
            print_list(eachItem,indent, level+1)
        else:
            if indent:
                for tab in range(level):
                    print("\t" * level,end="")
            print(eachItem)

#調用函數時 未給檔案物件 仍會將資料印在螢幕上
def print_file(the_list, indent = False, level =0 ,fh=sys.stdout):
        for eachItem in the_list:
            if(isinstance(eachItem, list)):
                print_file(eachItem,indent, level+1, fh)
            else:
                if indent:
                    for tab in range(level):
                        print("\t" * level,end="", file=fh)
                print(eachItem, file=fh)


#移除重複項目　並回傳前三筆資料
def remove_multi(_list):
    unique_list = []
    for t in _list:
        if t not in unique_list: 
            unique_list.append(t)
    return unique_list[0:3]

#get file data by fileName
def get_data(file_name):
    try:
        #os.getcwd()
        #print(os.getcwd())
    
        #os.chdir('../nester/source')
        #print(os.getcwd())
        #os.getcwd()
        with open(file_name) as f: data = f.readline()
        return data.strip().split(',')
    except IOError as ioerror:
        print("IO error:" + str(ioerror))

#類別用法
def get_coach_data_org(file_name):
    try:
        with open(file_name) as f: 
            data = f.readline()
            templ = data.strip().split(',')
            return Athlete(templ.pop(0),templ.pop(0),templ)
    except IOError as ierror:
        print("IO Error: " + str(ierror))
