# 1 . add , sub, mul, div 함수 정의해보기

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a = 1
b = 2

c = add(a,b)
d = sub(a,b)
e = mul(a,b)
f = div(a,b)

print(c,d,e,f)

# 2 . len() 구현

def my_len(l):
    len=0
    for x in l:
        len+=1
    return len

a = [5,5,6,7,8,3]
b="I am a boy."
print(len(a),len(b))
print(my_len(a),my_len(b))