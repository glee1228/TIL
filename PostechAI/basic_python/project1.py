import sys

def main():  #main함수 구현
    for path in sys.argv:
        if "students.txt" in path:
            f = open(sys.argv[1], "r")
        else :
            f = open("students.txt", "r")
    s_dict={}
    for i in f.readlines():
        fillDict(s_dict,i)
    sortPrint(s_dict)

    while True:
        command = input("# ")
        menu=command.upper()
        print(menu)
        if menu =='SHOW':
            show(s_dict)
        elif menu =='SEARCH':
            input_num = input("STUDENT ID : ")
            search(s_dict,input_num)
        elif menu =='CHANGESCORE':
            input_num = input("STUDENT ID : ")
            changeScore(s_dict,input_num)
        elif menu =='ADD':
            input_num = input("STUDENT ID : ")
            add(s_dict, input_num)
        elif menu =='SEARCHGRADE':
            input_grade=input("Grade to search : ")
            searchGrade(s_dict,input_grade)
        elif menu =='REMOVE':
            input_num = input("STUDENT ID : ")
            remove(s_dict,input_num)
        elif menu =='QUIT':
            quit(s_dict)
            f.close()

def setGrade(avg):  #Grade 반환 함수
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade
def setAvg(mid,final): #Average 반환 함수
    avg = (mid+final)/2
    return avg
def fillDict(s_dict,line):  #스트링으로 입력받은 한줄의 문자열을 column에 맞게 딕셔너리 키와 밸류로 지정해주는 함수
    if line is not "\n" and line is not None:
        input_list=line.split("\t")
        #print(input_list)
        tmp_list=[]
        num = input_list[0]
        name = input_list[1]
        mid = int(input_list[2])
        final = int(input_list[3])
        avg = (mid+final)/2
        tmp_list.append(name)
        tmp_list.append(mid)
        tmp_list.append(final)
        tmp_list.append(avg)
        grade=setGrade(avg)
        tmp_list.append(grade)
        s_dict[num] = tmp_list
    else:
        pass
def sortPrint(s_dict):  #딕셔너리를 테이블 형태로 출력하는 함수(람다 함수를 이용하여 정렬)
    colPrint()
    sort_dict = sorted(s_dict.items(),key=lambda k:k[1][3],reverse=True)

    for line in sort_dict:
        num, [name,mid,final,avg,grade] = line
        print("%8s%15s%8d%10d%12.1f%6s"%(num,name,mid,final,avg,grade))

def sort(s_dict):   #딕셔너리를 정렬된 튜플형태로 반환하는 함수
    sort_tuple = sorted(s_dict.items(),key=lambda k :k[1][3],reverse=True)
    return sort_tuple

def colPrint(): #테이블 속성값 출력 함수
    print("Student        Name       Midterm     final   Average  Grade\n-------------------------------------------------------------")

def show(s_dict):   #정렬된 테이블형태의 딕셔너리 속성값 출력함수
    sortPrint(s_dict)

def search(s_dict,input_num):   #학번을 검색하고 해당 학번 딕셔너리의 key와 value를 출력하는 함수
    flag = False
    for key,value in s_dict.items():
        if key == input_num:
            flag =True
            colPrint()
            num = key
            [name,mid,final,avg,grade]=value
            print("%8s%15s%8d%10d%12.1f%6s"%(num,name,mid,final,avg,grade))

    if flag==False:
        print("NO SUCH PERSON.")

def changeScore(s_dict,input_num):  #딕셔너리에 학번을 입력하고 중간점수,기말점수를 입력받아 해당 점수로 수정하는 함수
    flag = False
    for key, value in s_dict.items():
        if key == input_num:
            flag = True
            num = key
            [name, mid, final, avg, grade] = value
            input_mof = input("Mid/Final? ")
            mof = input_mof.upper()
            if mof =='MID'or mof=='FINAL':
                input_score = input("Input new score : ")
                new_score = int(input_score)
                if mof =='MID':
                    colPrint()
                    print("%8s%15s%8d%10d%12.1f%6s" % (num, name, mid, final, avg, grade))
                    print("Score changed")
                    new_avg=setAvg(new_score,final)
                    new_grade=setGrade(new_avg)
                    print(new_grade)
                    s_dict[key] = [name, new_score, final,new_avg,new_grade]
                    print("%8s%15s%8d%10d%12.1f%6s" % (num, name, s_dict[key][1], final, s_dict[key][3], s_dict[key][4]))
                elif mof =='FINAL':
                    colPrint()
                    print("%8s%15s%8d%10d%12.1f%6s" % (num, name, mid, final, avg, grade))
                    print("Score changed")
                    new_avg = setAvg(mid, new_score)
                    new_grade = setGrade(new_avg)
                    s_dict[key] = [name, mid, new_score, new_avg, new_grade]
                    print("%8s%15s%8d%10d%12.1f%6s" % (num, name, mid, s_dict[key][2], s_dict[key][3], s_dict[key][4]))
                else :
                    break
            else:
                break

    if flag == False:
        print("NO SUCH PERSON.")

def add(s_dict,input_num):  #딕셔너리를 추가하는 함수
    flag = False
    for key,value in s_dict.items():
        if key==input_num:
            flag=True
            print("AlREADY EXISTS.")
    if flag==False:
        add_name = input("Name : ")
        add_mid = int(input("Midterm Score : "))
        add_final = int(input("Final Score : "))
        add_avg = setAvg(add_mid, add_final)
        add_grade = setGrade(add_avg)
        s_dict[input_num] = [add_name, add_mid, add_final, add_avg, add_grade]
        print("Student added.")

def searchGrade(s_dict,input_grade):    #성적을 입력하고 해당 성적의 딕셔너리를 검색하는 함수
    g = input_grade.upper()
    flag = False
    if g == 'A' or g=='B' or g=='C' or g=='D' or g=='F':
        for key,value in s_dict.items():
            if value[4] == g:
                flag =True
        if flag ==True:
            colPrint()
            for key,value in s_dict.items():
                if value[4]==g:
                    print("%8s%15s%8d%10d%12.1f%6s" % (key,value[0], value[1], value[2], value[3], value[4]))

        else :
            print("NO RESULTS.")

def remove(s_dict,input_num):   #딕셔너리를 제거하는 함수
    flag = False
    del_num =''
    for key, value in s_dict.items():
        if key == input_num:
            flag = True
            del_num = key

    if flag==False:
        print("NO SUCH PERSON.")
    else :
        del s_dict[del_num]
        print("Student removed.")
def quit(s_dict):   #종료하는 함수(종료하기 전 프로그램상의 존재하는 딕셔너리를 평균값 기준으로 정렬하고 지정한 텍스트파일로 저장하는 함수)
    input_msg =input("Save data?[yes/no] ")
    end_or_not = input_msg.upper()
    if end_or_not =='YES':
        sorted_tuple = sort(s_dict)
        filename = input("File name : ")
        f2=open(filename,"w")
        for i in range(0,len(sorted_tuple)):
                num = sorted_tuple[i][0]
                name = sorted_tuple[i][1][0]
                mid = sorted_tuple[i][1][1]
                final = sorted_tuple[i][1][2]
                f2.write("%s\t%s\t%d\t%d\n"%(num,name,mid,final))
        f2.close()
        sys.exit()
    else:
        sys.exit()

main()