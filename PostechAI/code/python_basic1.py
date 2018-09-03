# 1. 화씨 온도를 섭씨온도로 변환하기
"""
F_temperature = int(input("화씨온도를 입력하세요 : "))
C_temperature = (F_temperature-32)*(5/9)
print(C_temperature)
"""

# 2 . 돈과 물건을 입력받아, 잔돈을 계산하여 출력하기, 동전개수는 최소화
"""
money = int(input("금액을 입력하세요 : "))
allmoney = money
five = 0
one = 0
temp = 0
while True:
    money = money - 500
    if money>0 :
        five+=1
    else :
        temp = money +500

        break

for i in range(1,5) :
    if 100 * i ==temp:
        one = i
        break

print("투입 금액은 {} 원 입니다".format(allmoney))
print("오백원 짜리 개수는 {} 개 입니다".format(five))
print("백원 짜리 개수는 {} 개 입니다".format(one))
"""

# 3 . 문자열 확인
"""
word = 'Postech AI Program'

if 'Postech' in word:
    print("포스텍 AI 교육생입니다")
else:
    print("일반 교육생입니다")
"""
# 4 . 문자열 관련 함수
"""
# len()
python = 'Python'
print(len(python))

# count()
s = 'Python is fun!'
print(s.count('n'))

#index()
s2 = 'AI is Cool'
print(s2.index('i'))

#join()
a =','
print(a.join('1234'))


# split()
s3 = 'Postech is fun'
print(s3.split())   # 공백으로 분리

s4 = 'one:two:three'
print(s4.split(':'))

print(s4)
"""

# 5 . 리스트 수정
"""
a = [ 1 , 2 , 3 ]
a[2] = 8
print(a)
print(a[1:2])
a[1:2] = ['a','b','c']
print(a)
a[1:4] =[]
print(a)
del(a[0])
print(a)
"""
# 6 . 리스트 패킹, 언패킹

#패킹
b2 = [1,2,3]
#언패킹
a,b,c = b2
print(a,b,c)


# 7. 날짜 출력 형식 변환

datestr = input("날짜(연/월/일)입력 : ")
datelist = datestr.split('/')
tenlater=int(datelist[0])+10
datelist[0] = str(tenlater)
print("입력한 날짜의 10년 후는 {0}년 {1}월 {2}일".format(tenlater,datelist[1],datelist[2]))