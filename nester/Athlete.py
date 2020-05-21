def sanitize(time_str):
    if '-' in time_str:
        splitter = '-'
    elif ':' in time_str:
        splitter = ':'
    else:
        return(time_str)

    (mins, second) = time_str.split(splitter)
    return (mins + '.' + second)

class Athlete:
    def __init__(self, _name, _bir=None, _time=[]):
        self.name = _name
        self.bir = _bir
        self.time= _time

    def how_big(self):
        return (len(self._time))
    
    def top3(self):
        return sorted(set([sanitize(t) for t in self.time]))[0:3]

    def add_time(self,time):
        self.time.append(time)

    def add_times(self, list_times):
        self.time.extend(list_times)

#繼承List 的新類別
class AthleteList(list):
    def __init__(self, _name, _bir=None, _time=[]):
        list.__init__([])
        self.name =_name
        self.bir =_bir
        #self.time =_time 資料本身就是list 所以不需要多一個timeList
        self.extend(_time)
    
    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]
