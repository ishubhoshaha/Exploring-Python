import sys

def BinarySearch(arr = [], searchItem = 0, length = 0):
    print arr
    start = 0
    end = length-1
    while(start<end):

        mid = (start+end)/2
        print arr[mid]
        if arr[mid] == searchItem:
            return mid
        if arr[mid]>searchItem:
            end = mid
        elif arr[mid]<searchItem:
            start = mid+1

    return "Item Not found in this list"

lst = [5,1,6,8,9,3]
print BinarySearch(sorted(lst),3,len(lst))
