"""
このファイルに解答コードを書いてください
"""

f = open('input.txt', 'r', encoding='UTF-8')


#print(f)
with open('input.txt') as f:
    l = f.readlines()
    check_num = int(l[len(l)-1])
    #print(check_num)
    result = check_num

    #print(l)
    dict={}
    lists_n =[]
    result_list=[]

    for i in range(len(l)-1):

        #print(l[i])
        index = l[i].find(':')
        #print(index)
        num = int(l[i][:index])
        lists_n.append(num)
        #print(num)
        #print('7')
        strs = l[i][index+1:].replace( '\n' , '' )
        if check_num % num==0:

            dict[num]= strs
            result_list.append(num)
    print(dict)
    #print(result_list)
    result_list= sorted(result_list)
    #print(result_list)
    for i in range(len(result_list)):
    #    print(dict[result_list[i]])
        if i ==0:
            result = dict[result_list[i]]
        else:
            result+= dict[result_list[i]]

    #print(result)
        #print(strs)



    f.close()
