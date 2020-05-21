import os
import pickle
from nester import print_file


def GetFile():
    #check file
    #if not os.path.exists('sketch.txt'):
    #    print('The file is missing!')
    #else:
    try:
        #當前的目錄工作位在何處
        os.getcwd()
        os.chdir('../nester/source')
        os.getcwd()

        #開啟檔案
        data = open('sketch.txt')
        '''print(data.readline(),end="")
        print(data.readline(),end="")

        print('seek(0) > 返回開頭\n')
        data.seek(0)'''

        man =[]
        otherMan= []
        for each_Line in data:
            #not 相反, find() 有找到會還傳字元index
            #if not each_Line.find(':') == -1 :
            try:
                (role, line_spoken) = each_Line.split(':',1)
                line_spoken = line_spoken.strip() #移除空白
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    otherMan.append(line_spoken)
                '''print(role, end='')
                print(' said: ')
                print(line_spoken,end='')'''
            except ValueError:
                pass #exception > 略過處理

    except IOError as err:
        print('The file is missing!\n' + str(err))
    finally:
        #locals() > 搜尋字串
        if 'data' in locals():
            data.close() #關閉檔案

    #把兩個角色的台詞分別寫入檔案
    try:
        # w:寫入檔案 若檔案不存在會新增
        # a:append
        print(man)
        #with 可免除finally suit 類似using會自動關閉
        #manData = open('man_data.txt',"w")
        with open('man_data.txt','w') as manData:
            #寫入檔案並印出
            print_file(man,fh=manData)
        
        #otherData = open('other_data.txt',"w")
        with open('other_data.txt','w') as otherData : 
            print_file(otherMan, fh=otherData)

        
    except IOError as err:
        print_file('file writer exception!\n' + str(err))

    '''finally:
        #close
        manData.close()
        otherData.close()'''

def GetFileByPickle():

    try:
        #當前的目錄工作位在何處
        os.getcwd()
        os.chdir('../nester/source')
        os.getcwd()

        #開啟檔案
        data = open('sketch.txt')
        '''print(data.readline(),end="")
        print(data.readline(),end="")

        print('seek(0) > 返回開頭\n')
        data.seek(0)'''

        man =[]
        otherMan= []
        for each_Line in data:
            #not 相反, find() 有找到會還傳字元index
            #if not each_Line.find(':') == -1 :
            try:
                (role, line_spoken) = each_Line.split(':',1)
                line_spoken = line_spoken.strip() #移除空白
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    otherMan.append(line_spoken)
                '''print(role, end='')
                print(' said: ')
                print(line_spoken,end='')'''
            except ValueError:
                pass #exception > 略過處理

    except IOError as ferr:
        print('The file is missing!\n' + str(ferr))
    finally:
        #locals() > 搜尋字串
        if 'data' in locals():
            data.close() #關閉檔案

       
    #把兩個角色的台詞分別寫入檔案
    try:
        new_man = []
        new_other = []
        with open('man_data.txt','wb') as save_data, open('other_data.txt','wb') as othersave_file:
            pickle.dump([1,2,'three'], save_data)
            pickle.dump([1,2,'three',4,5,6], othersave_file)
            #pickle.dump(man,man_file)
            #pickle.dump(otherMan,other_file)
        with open('man_data.txt','rb') as man_file, open('other_data.txt','rb') as other_file:
            #dump:保存資料  load:復原資料
            new_man = pickle.load(man_file)
            new_other = pickle.load(other_file)
        print_file(new_man)
        print_file(new_other)
            #print(man)
    except IOError as err:
        print('File error' + str(err))
    except pickle.PicklingError as perror:
        print('pickle error: ' + str(perror))

def PickleTest():
    try:
        with open('pickle.txt','wb') as save_data:
            pickle.dump([1,2,'three'], save_data)

        with open('pickle.txt','rb') as restore_data:
            a_list = pickle.load(restore_data)
        print(a_list)
    except pickle.PicklingError as peer:
        print('pickle Error:'+ str(peer))
#print('call Get File')
#GetFile()

print('pickle:')
GetFileByPickle()
#PickleTest()