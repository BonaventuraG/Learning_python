def my_method(list,list2,var):
    print(var,end=' ')
    var+=1
    print(var)
    list.append(var)
    list2=[0,0,0]
    print(id(list2))
    return 0