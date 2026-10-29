def count_common_unique(list1, list2):
    # list1: list of strings
    # list2: list of strings
    # return an integer
    dict1 = {}
    dict2 = {}
    set1= set()
    set2= set()
    for i in list1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for i in list2:
        if i in dict2:
            dict2[i]+=1
        else:
            dict2[i]=1
    for i,k in dict1.items():
        if k<=1:
            set1.add(i)
    for i,k in dict2.items():
        if k<=1:
            set2.add(i)
    result = list(set1.intersection(set2))
    return len(result)
    
    
    pass