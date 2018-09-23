
def main():
    healths=[200,120,150]
    influ=[]
    items=[]
    attack=[30,500,100]
    minus=[100,30,400]

    for i in range(0,3):
        influ.append(attack[i])
        influ.append(minus[i])
        items.append(influ)
        influ=[]
    solution(healths,items)


def solution(healths,items):
    answer =[]
    healths.sort() # healths 오름차순 정렬
    items2 = sorted(items, key=lambda k: k[1]) #item의 체력마이너스 기준으로 오름차순 정렬
    print(items2)
    print(healths)
    check=9999 #체력이 마이너스가 안되는 index를 저장하는 변수
    for i in range(0,len(items2)):
        for j in range(0,len(healths)):
            if items2[i][1]-healths[j]>0:
                check=j # 체력이 마이너스 안되는 index
                break

    for i in range(check,len(items2)):
        answer.append(items2)

    return answer

main()