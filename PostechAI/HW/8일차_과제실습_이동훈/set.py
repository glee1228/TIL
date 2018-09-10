class Set:
    def __init__(self, member=[]):
        self.member=member
    def append(self, a):
        tmp=[]
        tmp=self.member+a.member
        result = set(tmp)
        return list(result)
    def delete(self, a):
        tmp =Set(self.member)
        for i in a.member:
             if i in tmp.member:
                 tmp.member.remove(i)
        return tmp.member
    def union(self, s2):
        tmp = []
        for i in range(0,len(self.member)):
            tmp.append(self.member[i]+s2.member[i])
        return tmp

    def intersection(self, s2):
        tmp = []
        for i in range(0,len(self.member)):
            section=int(self.member[i]/s2.member[i])
            tmp.append(section)
        return tmp
    def difference(self, s2):
        tmp = []
        for i in range(0,len(self.member)):
            diff = self.member[i]-s2.member[i]
            tmp.append(diff)
        return tmp
    def __add__(self,another):
        tmp = []
        for i in range(0, len(self.member)):
            tmp.append(self.member[i] + another.member[i])
        return tmp
    def __truediv__(self, another):
        tmp = []
        for i in range(0, len(self.member)):
            section = int(self.member[i] / another.member[i])
            tmp.append(section)
        return tmp
    def __sub__(self,another):
        tmp = []
        for i in range(0, len(self.member)):
            diff = self.member[i] - another.member[i]
            tmp.append(diff)
        return tmp
a = Set([1, 2, 3])
b = Set([2, 3, 4])

c = a.union(b)
print(c)
d = a.difference(b)
print(d)
e = a.intersection(b)
print(e)
f = a+b
print(f)
g = a/b
print(g)
h = a-b
print(h)