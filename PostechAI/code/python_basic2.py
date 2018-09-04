# 1 . 영어 수학 합불 판별
"""
eng = int(input("영어 성적 입력 : "))
math = int(input("수학 성적 입력 : "))
all = eng+math

if all>=110:
    print("합격")
else :
    if math<40:
        print("불합격 : 수학점수 부족")
    elif eng<40:
        print("불합격 : 영어점수 부족")
    else:
        print("불합격 : 총합점수 부족")
"""


# 2 . 세 개의 정수를 입력받아 가장 큰 수만 출력
"""
num = []
print("세 개의 정수를 입력하세요")
for i in range(0,3):
    num.append(input(""))

print("가장 큰 수는 ",end='')
if num[0]>=num[1]:
    if num[0]>=num[2]:
        print(num[0])
    else :
        print(num[2])
else :
    if num[1]>=num[2]:
        print(num[1])
    else :
        print(num[2])
"""

# 3 . 1부터 10까지의 합
"""
total =0
for i in range(1,11):
    total +=i

print("1부터 10까지의 합은 {0} 입니다".format(total))
"""

# 4 . 구구단 출력
"""
gugudan = int(input("출력하고 싶은 단을 입력하세요 : "))

for i in range(1,10):
    print("{0} * {1} = {2}".format(gugudan,i,gugudan*i))
"""

# 5 . * 출력 프로그램
"""
star_str = input("Input an integer : ")

for i in range(0,len(star_str)):
    for j in range(0,int(star_str[i])):
        print("*",end="")
    print()
"""

# 6 . "done"을 입력할 때까지 숫자 입력 받고, "done"을 입력할 때 리스트의 평균, 최대값과 최소값 출력하는 프로그램
"""
numlist =[]
while True:
    tmp_str = input("Enter a number : ")
    if tmp_str =="done":
        break
    tmp_num = int(tmp_str)
    numlist.append(tmp_num)

listsum = sum(numlist,0.0)
listavg = listsum/len(numlist)

print("Average : {0}".format(listavg))
print("Maximum : {0}".format(max(numlist)))
print("Minimum : {0}".format(min(numlist)))
"""

# 7 . 문장을 입력받아 해당 문장에서 각 알파벳이 몇 개씩 나오는지 저장하는 딕셔너리 만들고 출력
"""
a_dict={}
sentence = input("Enter a sentence : ")
for i in range(0,len(sentence)):
    if sentence[i] not in a_dict.keys():
        a_dict[sentence[i]]=1
    else :
        a_dict[sentence[i]]+=1

print(a_dict.items())
"""

# 8 . 입력 받은 정수 홀수 짝수 판별
"""
oddoreven = int(input("정수 하나 입력 : "))

if oddoreven%2==0:
    print("짝수입니다")
else:
    print("홀수입니다")
"""

# 9 . 중간, 기말고사 점수 입력받고 평균, 등급 출력
"""
mid = int(input("Enter your midterm score: "))
final = int(input("Enter your final score: "))

score_avg = (mid+final)/2

print("Average : {0}".format(score_avg))
if score_avg >=90:
    print("A")
elif score_avg >=80:
    print("B")
elif score_avg >=70:
    print("C")
elif score_avg >=60:
    print("D")
else:
    print("F")
"""

# 10 . 문자열 반복 출력(while)
"""
input_msg1 = input("word = ")
m=0
while m<len(input_msg1):
    print("{0}".format(input_msg1[m]))
    m+=1
"""

# 11 . 문자열 반복 출력(for)
"""
input_msg2 = input("word = ")
for i in range(0,len(input_msg2)):
    print("{0}".format(input_msg2[i]))
"""

# 12 . count down , happy new year!
"""
for i in range(0,10):
    print("{0}".format(10-i),end=', ')
print("Happy New Year! ")
"""

# 13 . 정수 a부터 정수 b 까지의 합 구하는 프로그램
"""
input_msg3 = input("Enter two Integers : ")
num = input_msg3.split()
a = int(num[0])
b = int(num[1])
total =0
for i in range(a,b+1):
    total+=i
print("The sum from {0} to {1} is {2}".format(a,b,total))
"""

# 14 . 주어진 문자열에 'a'가 몇개 있는지 검출하기
"""
input_msg4 = input("word = ")
a_count=0
for i in range(0,len(input_msg4)):
    if input_msg4[i]=='a':
        a_count+=1

print("Count 'a' : {0}".format(a_count))
"""

# 15 . for문과 range 함수 써서 출력해보기
"""
for i in range(0,10):
    print(i,end=' ')
print()
for i in range(0,11):
    print(i*5,end=' ')
print()
for i in range(0,10):
    print(10-i,end=' ')
print()
"""

# 16 . for 문을 사용하여 리스트의 모든 내용 출력하기 range 사용하지 않기!
"""
colors = ["red","green","blue"]
print(colors)
"""
# 17 . 리스트 방문하되 짝수만 출력
"""
a = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in range(0,len(a)):
    if a[i]%2==0:
        print(a[i],end=' ')
print()
"""

# 18 . 구구단 전체 출력
"""
for i in range(1,10):
    for j in range(1,10):
        print("{0} * {1} = {2}".format(i,j,i*j))
"""

# 19 . 주어진 문장 형식에 맞게 출력
"""
sentence = "sally goes to the store."

sentence_list = sentence.split()

for i in range(0,len(sentence_list)):
    print("sentence {0} : {1}".format(i+1,sentence_list[i]))
"""

# 20 . 문자열 줄 띄기 연습

print("{0} \n 안녕하세요".format(10))