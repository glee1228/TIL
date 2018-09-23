import math

class house:
    x = 100
    y = 100
    num_acounts=0
    ex=[]
    def __init__(self, x,y):
        self.x = x
        self.y = y
        house.num_accounts += 1
        house.ex.append(x,y)

class factory:
    x=100
    y=100
    num_accounts=0
    ex=[]
    def __init__(self,x,y):
        self.x=x
        self.y=y
        factory.num_accounts+=1
        factory.ex.append(x,y)

def main():
    N=1
    dist=[]
    it = house(100,100)
    available_dist(house,it,factory)

def available_dist(house,it,factory):
    global dist
    if it.x==house.ex[0] and it.y==house.ex[1]:
        return False
    elif it.x==factory.ex[0] and it.y==factory.ex[1]:
        return False
    else:
        for x in range(0,200):
            200-x
        dist.append(math.sqrt(math.pow((factory.ex[0]-it.x),2)+math.pow((factory.ex[1]-it.y),2)))



def solution(N,house):
    answer= 0

    y=100
    return answer
main()