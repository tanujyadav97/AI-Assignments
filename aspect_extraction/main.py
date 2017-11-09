import pickle
from bisect import bisect_left
import operator

file=open("data.pkl","r")
data=pickle.load(file)


def takeClosest(myList, myNumber):
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
       return after
    else:
       return before

aspects=[]

for i in range(1,len(data)):
    list=data[i][1]
    if len(list)>0:
        for noun in data[i][0]:
            if abs(takeClosest(list,noun[1])-noun[1]<=2):
                aspects.append(noun[0])


temp={}
for asp in aspects:
    temp[asp]=0

for asp in aspects:
    temp[asp]+=1


sorted_x = sorted(temp.items(), key=operator.itemgetter(1))
sorted_x.reverse()
aspects=[i[0].encode('utf-8') for i in sorted_x]
print("Extracted Aspects are:")
print aspects[:25]