
numRows=5

pList=[[1]]
# t1=list(pList[len(pList)-1])
# t1.append(0)

# print(t1)

if numRows>1:
    for i in range(1,numRows):
        p1=list(pList[len(pList)-1])
        p2=list(p1)
        p2.append(0)
        p1.insert(0,0)
        pList.append([sum(x) for x in zip(p1, p2)])
print(pList)