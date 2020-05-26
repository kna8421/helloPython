import os

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
            inner_dic[row[i]] = column_headings[i]
            
        row_data[row_label] = inner_dic

column_headings = row_data['15k']['43:24']
print(column_headings)

prediction = [k for k in row_data['20k'].keys() if row_data['20k'][k] == column_headings]
print(prediction)
'''num_cols =len(column_headings)
print(num_cols,end=' -> ')
print(column_headings)

num_cols = len(row_data['2mi'])
print(num_cols,end=' -> ')
print(row_data['2mi'])

num_cols = len(row_data['Marathon'])
print(num_cols,end=' -> ')
print(row_data['Marathon'])'''