import os
import find_it
from find_it import find_nearest_time, format_time, secs2time, time2secs

os.chdir('../nester/source')
row_data = {}
with open('PaceData.csv')as paces:
    column_headings = paces.readline().strip().split(',')
    column_headings.pop(0) #去掉第一個標題
    for each_line in paces:
        row = each_line.strip().split(',')
        row_label  =row.pop(0) #每列的第一個是列標籤
       # row_data[row_label] = row #用字典存資料
        inner_dic ={}
        for i in range(len(column_headings)):
            inner_dic[format_time(row[i])] = column_headings[i]
            
        row_data[row_label] = inner_dic

column_headings = row_data['15k'][format_time('43:24')]
print(column_headings)

prediction = [k for k in row_data['20k'].keys() if row_data['20k'][k] == column_headings]

'''prediction=[]
for k in row_data['20k'].keys():
    if row_data['20k'][k] == column_headings :
        prediction.append(k)'''
print(prediction)

'''age = input("What is your age: ")
print(age)
int(age)'''

#20k 59:59 Marathon -> 01:00:23
distance_run=input("Enter the distance attempted: ")
recorded_time = input('Enter the recorded time: ')
prediction_distance = input('Enter the distance you want a prediction for: ')

closet_time = find_nearest_time(format_time(recorded_time), row_data[distance_run])
closet_column_heading = row_data[distance_run][closet_time]

prediction = [k for k in row_data[prediction_distance].keys()
                    if row_data[prediction_distance][k] == closet_column_heading]
print('The predicited time running ' + prediction_distance + ' is : ' + prediction[0] + " .")

'''num_cols =len(column_headings)
print(num_cols,end=' -> ')
print(column_headings)

num_cols = len(row_data['2mi'])
print(num_cols,end=' -> ')
print(row_data['2mi'])

num_cols = len(row_data['Marathon'])
print(num_cols,end=' -> ')
print(row_data['Marathon'])'''