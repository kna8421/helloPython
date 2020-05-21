#Format 若是運算式{0},若為物件可直接{}
#也可以用變數命名'{id}{name}'.format(id='1',name='test')

#LIST 運用
lists =['apple', 'pen', 'pen', 'pineapple']
print('List尾端增加元素 100:')
lists.append(100)
print(lists)

print('\n用.JOIN的方式 把List取出')
'''LIST包含數字 不能直接轉成字串。
solition：print(" ".join('%s' %id for id in list1))
'''
print(",".join('%s' %item for item in lists))

lists.remove(100)
lists.append('aaa')
print(','.join(lists))

#tuple 也可以這樣運用
print('\n取出前兩個元素 連接在一起:')
print(lists[0] + lists[1])

print('\n刪除第二個元素:')
del lists[2]
print(lists)

print('\n最後元素改為cup :')
lists[3] = 'cup'
print(lists)

print('\n將pen插入第二個元素:')
lists.insert(2, 'pen')
print(lists)

print('\nList 增加另一個list')
lists.extend(["add1","add2"])
print(lists)

print('\n移出最後一個')
lists.pop()
print(lists)

#tuple : 不可複寫的元組, 可以作為Dic的key
tuple = ('apple', 'pen', 'pen', 'pineapple')
print('\n--------------tuple: --------------------')
print(tuple)
print('\n\n連接前兩個tuple: {0}'.format(tuple[0] + tuple[1]))


#切割(Slice) and Len > List和Tuple都可用
print('\n\n取第二個之前的元素: ')
print(lists[0:2])
print(tuple[0:2])

print('\n\n從第一取到最後的元素: ')
print(lists[1:])
print(tuple[1:])

print('\n\nList和tuple的長度: ')
print(len(lists))
print(len(tuple))

#Set : 和List Tuple類似,但是set 沒有順序性 且不允許重複的陣列
uniq = set(['apple', 'pen', 'pen', 'pineapple'])
print('\n\n Set: {}'.format(uniq))
#只會印出 {'pineapple', 'apple', 'pen'} 重複不會出錯 只會印出一個

uniq.add('banana')
print('\n\nset.add banana : {}'.format(uniq))

uniq.remove('pen')
print('\n\nset.remove pen : {}'.format(uniq))


#Set的運算 :檢查Set是否包含某一職,包刮 關係 交集 聯集 插集
uniq = set(['apple', 'pen', 'pen', 'pineapple'])
a = set(['apple', 'pen'])
b = set(['pen', 'pineapple'])
print('\nuniq: {}'.format(uniq))
#print(uniq)
print('\na: {}'.format(a))


print('\nSet-a是否被uniq 包含')
print(a.issubset(uniq))

print('\nSet-a 裡是否含有pen: {0}'.format('pen' in a))

print('\nSet-a 裡是否含有PEN: {0}'.format('PEN' in a))

print('\nSet-a 裡是否含有banana: {0}'.format('banana' in a))


print('\nb: {}'.format(b))

print('\na b 交集')

print(a.intersection(b))

print('\na b 聯集(全部元素)')
print(a.union(b))

print('\na b 差集(只在a的元素)')
print(a.difference(b))

#Dict
empty_dic = {}
empty = dict() 
dict1 = {'apple':1, 'pen':2, 'pineapple':3}
print('\n\nDict')
print(dict1)

print('\n指定key:pen取得value')
print(dict1['pen'])

print('\n將key用List取出')
print(dict1.keys())

print('\n將value用List取出')
print(dict1.values())

print('\nDict新增指定key value')
dict1['banana']=5
print(dict1)

print('\n刪除key為banana')
dict1.pop('banana')
print(dict1)

print('\n修改指定key的value')
dict1['pen']=100
print(dict1)

'''Sequence 運算

'''

#方法
def over(num, thres):
    if num > thres:
        print(str(num) + ' > ' + str(thres))
    else:
        print(str(num) + ' <= ' + str(thres))
print('\ncall over')
over(333,100)
over(-1,10)

# List 轉成 set型別
def include(list, keyword):
    uniq = set(lists)
    if keyword in uniq:
        print('含有' + keyword)
    else:
        print('不包含' + keyword)

#迭代
print('\n迭代')
for item in lists:
    print(item)

names = ['Melissa','micasa',['este','estrella','essabbina']]

print(isinstance(names, str))
print(isinstance(uniq, set))


#列印清單
def print_list(the_list,indent = False, level=0):
    for eachItem in the_list:
        if(isinstance(eachItem, list)):
            print_list(eachItem,indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t" * level,end="")
            print(eachItem)


print('\ncall print_list:')
print_list(names,5)

#Range
# end="" 可以拿掉print()自動加上得換列功能
print('print range(4):',end="")
for num in range(4):
    print(num,end="")

