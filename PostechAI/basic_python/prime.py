
def main():
    a = 13
    b = 15
    if check_prime(a):
        print(str(a)+"는 소수입니다")
    else:
        print(str(a)+"는 소수가 아닙니다")

    if check_prime(b):
        print(str(b)+"는 소수입니다")
    else :
        print(str(b)+"는 소수가 아닙니다")

def check_prime(num):
    cdlist=[]
    for x in range(1,num+1):
        if num%x==0:
            cdlist.append(x)
    cdlist.remove(x)
    if max(cdlist)==1:
        return True
    else:
        return False

main()