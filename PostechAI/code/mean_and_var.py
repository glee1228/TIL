def main():
    v1 = (0,1)
    v2 = (0.5,0.5)
    v3 = (1,0)

    m,var = mean_and_var(v1,v2,v3)
    print("평균 : {0}, 분산 : {1}".format(m,var))

def mean_and_var(v1,v2,v3):


    mean0=(v1[0]+v2[0]+v3[0])/3
    mean1=(v1[1]+v2[1]+v3[1])/3
    var0 = (pow((v1[0]-mean0),2)+pow((v2[0]-mean0),2)+pow((v3[0]-mean0),2))/3
    var1 = (pow((v1[1] - mean1), 2) + pow((v2[1] - mean1), 2) + pow((v3[1] - mean1), 2)) / 3
    mean=(mean0,mean1)
    var=(var0,var1)
    return mean,var

main()