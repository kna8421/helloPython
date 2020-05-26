import time

def find_closest(look_for, target):
    def whats_the_diff(first, second):
        if first == second:
            return (0)
        elif first > second:
            return (first - second)
        else:
            return (second - first)
    
    max_diff = 9999999
    for each in target:
        diff = whats_the_diff(each, look_for)
        if diff == 0:
            found_it = each
            break
        elif diff < max_diff:
            max_diff = diff
            found_it = each
    return found_it


#時間轉換 HH:MM:SS
def format_time(time_str):
    tlen = len(time_str)
    if tlen <3:
        original_format = '%S'
    elif tlen < 6:
        original_format = '%M:%S'
    else:
        original_format='%H:%M:%S'
    time_str = time.strftime('%H:%M:%S', time.strptime(time_str, original_format))
    return time_str

#時間轉換 以秒為單位
def time2secs(time_str):
    time_str = format_time(time_str)
    (h,m,s) =time_str.split(':')
    seconds = int(s) + (int(m) * 60) + (int(h) * 60 * 60)
    return seconds

#時間轉換 秒轉成時間字串
def secs2time(seconds):
    return time.strftime('%H:%M:%S', time.gmtime(seconds))


def find_nearest_time(look_for,target_data):
    what = time2secs(look_for)
    #清單中的時間字串轉換成秒數
    where = [time2secs(t) for t in target_data]
    res = find_closest(what, where)
    return secs2time(res)

#test
test = find_nearest_time('59:59', ['56:29','57:45','59:03','1:00:23','1:01:45'])
print(test)

test = find_nearest_time('57:06',['56:29','57:45'])
print(test)

test = find_nearest_time('1:01:01',['59:03','1:01:23','1:01:45'])
print(test)


result = find_closest(3.3,[1.5,2.5,4.5,5.2,6])
print(result)

result = find_closest(3,[1,5,6])
print(result)

result = find_closest(3,[1,3,4,6])
print(result)

result = find_closest(3,[1,4,6])
print(result)