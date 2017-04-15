def BubbleSort(lst):
    n = len(lst)
    for k in range(n-1): # upto n-1
        for i in range(n-k-1):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i] #Swap
    return lst 
lst = [111,-70,-2,4,9,1,-8,7]
print "After Sorting: ", 
print BubbleSort(lst)
