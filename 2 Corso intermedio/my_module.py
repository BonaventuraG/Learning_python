def my_method(list1,var):
    print(id(var),var)
    var+=1
    print(id(var),var)
    print(id(list1),list1)
    list1.append(var)
    print(id(list1),list1)
    return 0