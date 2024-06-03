import copy
numRows=5

pList=[[1]]

if numRows>1:
    for i in range(1,numRows):
        p1=pList[len(pList)-1]
        p2=list(p1)
        p2.append(0)
        p1.insert(0,0)

        print(p1,p2)