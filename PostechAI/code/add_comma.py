def main():
    comma_added_1234 = add_comma(1234)
    comma_added_12345678 = add_comma(12345678)
    comma_added_12 = add_comma(12)

    print(comma_added_1234)
    print(comma_added_12345678)
    print(comma_added_12)

def add_comma(num):
    num_str = str(num)
    list_num=list(num_str)
    list_num.reverse()
    result_list =[]
    for x in range(0,len(list_num)):
        if x%3==0 and x!=0:
            result_list.append(',')
        result_list.append(list_num[x])
    result_list.reverse()
    result_str= "".join(result_list)
    return result_str

main()