class NamedList(list):
    def __init__(self, _name):
        #初始化被衍生類別 然後將引數賦值給屬性
        list.__init__([])
        self.name = _name


potter = NamedList("Harry James Potter")
print(type(potter))
print(dir(potter))

print(potter.name)
potter.append("Good_At")
potter.extend(['Quidditch','Defense Against the Dark Arts','Save'])
print(potter)


