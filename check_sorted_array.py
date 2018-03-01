a = [3,2,1]
all(a[i] <= a[i+1] for i in range(len(a)-1))
