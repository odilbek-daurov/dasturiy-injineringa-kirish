def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(1,len(lst)-i):
            if lst[j-1]>lst[j]:
                temp = lst[j-1]
                lst[j-1] = lst[j]
                lst[j] = temp
    return lst
lst = [1,-8,2,-8,8,6,-1,0,5]
#pufakchali saralash
