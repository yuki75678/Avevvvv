"""
このファイルに解答コードを書いてください
"""

#f = open('input.txt', 'r', encoding='UTF-8')


#read data
with open('input.txt') as f:
    l = f.readlines()
    check_num = int(l[len(l)-1])
    #save result
    result = check_num

    #prepare dict and save_data
    dict={}
    lists_n =[]
    result_list=[]

    #pull data
    for i in range(len(l)-1):

        #print(l[i])
        index = l[i].find(':')
        #print(index)
        num = int(l[i][:index])
        lists_n.append(num)

        strs = l[i][index+1:].replace( '\n' , '' )
        if check_num % num==0:

            dict[num]= strs
            result_list.append(num)
    #sort
    result_list= sorted(result_list)

    #create result by list
    for i in range(len(result_list)):
    
        if i ==0:
            result = dict[result_list[i]]
        else:
            result+= dict[result_list[i]]

    print(result)
        #print(strs)



    f.close()
