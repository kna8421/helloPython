import os
import pickle
from Athlete import Athlete, AthleteList, get_coach_data, sanitize
from nester import  get_coach_data_org, get_data, remove_multi

os.getcwd()
os.chdir('../nester/source')
os.getcwd()

clear_james=[]
clear_julie=[]
clear_mikey=[]
clear_sarah=[]
#簡單直覺版
with open('james.txt') as ja: data = ja.readline();
james = data.strip().split(',')
for t in james:
    clear_james.append(sanitize(t))
print(sorted(set(clear_james)))


with open('julie.txt') as ju:data = ju.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mi: data = mi.readline()
mikey = data.strip().split(',')


#list comprehension
#set去除重複直
clear_julie = sorted(set([sanitize(t) for t in julie]))
clear_mikey = remove_multi(sorted([sanitize(t) for t in mikey]))

print(clear_julie[0:3])
#print(clear_mikey)

#方法化
sarah = get_data('sarah.txt')
#(sarah_name, sarah_bir) = sarah.pop(0),sarah.pop(0)
sarah_dict = {}
sarah_dict['Name'] = sarah.pop(0)
sarah_dict['Birthday'] = sarah.pop(0)
clear_sarah = sorted(set([sanitize(t) for t in sarah]))
print(sarah_dict['Name'] + '\'s fastest records are : ' + str(clear_sarah[0:3]))

#類別用法
sarah = get_coach_data_org('sarah.txt')
print(sarah.name + "'s birthday is " + str(sarah.bir))

print(sarah.name + "'s fastest records are : " + str(sarah.top3()))

sarah.add_time("2.33")
print(sarah.name + "'s fastest records are : " + str(sarah.top3()))

sarah.add_times(["2.32","2.30"])
print(sarah.name + "'s fastest records are : " + str(sarah.top3()))

vera= AthleteList('Vera Vi')
print(vera.name + ' : AthleteList')
vera.append('1.31')
print(str(vera.top3()))
vera.extend(['2.22','1-21','2:22'])
print(str(vera.top3()))

james = get_coach_data('james.txt')
james.name = "James"
print(james.name + "'s fastest records are : " + str(james.top3()))