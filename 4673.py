selfnum = list(range(1,10001))
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                ele = 1001*a + 101*b + 11*c +2*d
                if ele in selfnum:
                    selfnum.remove(ele)
for i in selfnum:
    print(i)