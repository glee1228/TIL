# 1 . 문장을 입력받아 해당 문장에서 각 알파벳이 몇 개씩 나오는지 저장하는 딕셔너리 만들고 출력
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

# 2 . 파일에 있는 각각의 단어의 수 구하기
"""
f = open("test.txt","r")
txt_dict={}
for line in f:
    lines2 = line.split()
    for i in lines2:
        if i not in txt_dict.keys():
           txt_dict[i] = 1
        else :
            txt_dict[i] +=1

print(txt_dict.items())
"""

# 3 . 딕셔너리 타입의 d의 모든 value 출력
"""
d = {'youn': 1, 'park': 2, 'kim': 10}

print(d.values())
"""

# 4 . 딕셔너리 알파벳 기준으로 순서대로 key,value를 출력
"""
d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
sorted_list = sorted(list(d.keys()))
print(sorted_list)
for i in range(0,5):
     print(str(d[sorted_list[i]])+" "+sorted_list[i])
"""

# 5 . 파일명을 입력 받아 , 해당 파일을 한 줄 씩 읽어 파일 내용을 전부 대문자로 출력하기
"""
f = open("test.txt","r")
txt_dict={}
for line in f:
    line2 = line.upper()
    print(line2,end='')
"""

# 6 . 리눅스 쉘에서 원본 파일명과 사본파일명을 입력 받아 복사하는 프로그램



# 7 . 아래의 score.txt를 읽어서 학생들의 성적을 처리하여 그 결과를 report.txt로 출력하는 프로그램 작성
"""
grade =""
mid_tmp =""
final_tmp =""
f = open("score.txt","r")
f2 = open("report.txt","a")
for line in f:
    line2=line.split()
    for token in line2:
        if len(token)==6:
            stunum = token
        elif line2[1]==token:
            mid_tmp = token
        else :
            final_tmp = token
    mid = int(mid_tmp)
    final = int(final_tmp)
    total=(mid*4+final*6)/10
    if total>=90:
        grade = 'A'
    elif total>=80:
        grade = 'B'
    elif total>=70:
        grade = 'C'
    elif total>=60:
        grade = 'D'
    else :
        grade = 'F'
    f2.write(stunum+" "+str(mid)+" "+str(final)+" "+str(total)+" ("+grade+")\n")

f2.close()
f.close()
"""
