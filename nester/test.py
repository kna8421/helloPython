import os

os.getcwd()

os.chdir('../nester/source')
os.getcwd()

#開啟檔案
data = open('sketch.txt')

for each_Line in data:
    (a,b) = each_Line.split(":",1)