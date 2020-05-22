
class AthleteList(list):

    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    @staticmethod
    def sanitize(time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return(time_string)
        (mins, secs) = time_string.split(splitter)
        return(mins + '.' + secs)

    #方法已被指派成類別特性　top3()傳回的資料就像是一個類別屬性，所以呼叫不能加() 要直接top3呼叫
    @property
    def top3(self):
        return(sorted(set([self.sanitize(t) for t in self]))[0:3])

    @property
    def clean_data(self):
        return(sorted(set([self.sanitize(t) for t in self])))

    #Json不能處理字定義的類別 但是可以支援Python內建的類別 所以要把類別屬性資料轉換成字典
    @property
    def as_dict(self):
        return({'Name': self.name,
                'DOB': self.dob,
                "Top3": self.top3})