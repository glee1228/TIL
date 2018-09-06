import random


def main():
    a = []
    for i in range(10):
        a.append(random.randint(1, 10))
    print(a)
    lcm_value = LCM(a)
    gcd_value = GCD(a)
    print("최소공배수 : {0} , 최대공약수 : {1} ".format(lcm_value, gcd_value))


def LCM(l):
    max_num = max(l)
    lcm = max_num
    count = 0
    while True:
        for x in l:
            if lcm % x == 0:
                count += 1
        if count == 10:
            break
        else:
            lcm += 1
        count = 0

    return lcm


def GCD(l):
    gcd_dict = {}
    gcd = 0
    for x in l:
        cdlist = CD(x)
        for y in cdlist:
            if y not in gcd_dict.keys():
                gcd_dict[y] = 1
            else:
                gcd_dict[y] += 1
    for key, value in gcd_dict.items():
        if value == 10:
            gcd = key
    return gcd


def CD(num):
    cd = []
    idx = 2
    for x in range(1, num + 1):
        if num % x == 0:
            cd.append(x)
    return cd


main()