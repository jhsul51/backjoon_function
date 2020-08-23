def verify(number):
    n = [int(i) for i in str(number)]
    temp = 0
    for i in range(len(n)-1):
        if i==0:
            diff = n[i+1] - n[i]
            temp = diff
        else:
            diff = n[i+1] - n[i]
            if temp != diff:
                return False
    return True

x = int(input())
count = 0
for i in range(1,x+1):
    if verify(i):
        count += 1
print(count)