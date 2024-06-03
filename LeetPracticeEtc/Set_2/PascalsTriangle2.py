rowIndex=3

pList=[[1]]

if rowIndex==0: print(pList[0])
else:
    for i in range(1,rowIndex+1):
        p1=list(pList[len(pList)-1])
        p2=list(p1)
        p2.append(0)
        p1.insert(0,0)
        pList.append([sum(x) for x in zip(p1, p2)])
    print(pList[rowIndex])