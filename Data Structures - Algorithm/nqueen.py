import sys
column = [0]*100
def isSafe(row,col):
    for i in range(row):
        if(column[i]==col or abs(column[i]-col)==abs(i-row)):
            return False
    return True

def NQueen(row,n):
    for col in range(n):
        if(isSafe(row,col)):
            column[row] = col
            if row==n-1:
                lst = column[:n]
                print [x+1 for x in lst]
            else:
                NQueen(row+1,n)


n = int(raw_input())
NQueen(0,n)
