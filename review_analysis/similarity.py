import pickle
from scipy.stats import pearsonr

def takefirst(elem):
    return elem[0]

file=open("reviews.pkl","r")
data=pickle.load(file)

size= len(data)
mat=[[{} for x in range(10)] for y in range(size)]

keys=data.keys()
c1=0
c2=0
for k in keys:
    dict1=data[k]
    simi=[]
    for k1 in keys:
        if k!=k1:
            dict2=data[k1]
            keys1 = dict1.keys()
            keys2 = dict2.keys()

            list1 = []
            list2 = []

            for i in keys1:
                if i in keys2:
                    list1.append(float(dict1[i][1]))
                    list2.append(float(dict2[i][1]))
                else:
                    list1.append(float(dict1[i][1]))
                    list2.append(float(0))

            for i in keys2:
                if i not in keys1:
                    list2.append(float(dict2[i][1]))
                    list1.append(float(0))

            similirity2 = pearsonr(list1, list2)
            temp={}
            temp[0]=abs(similirity2[0])
            temp[1]=k1
            simi.append(temp)

    simi.sort(key=takefirst, reverse=True)

    for c2 in range(10):
        mat[c1][c2] = simi[c2]

    c1+=1
    if c1%10==0:
        print c1

output=open('matrix.pkl','wb')
pickle.dump(mat,output)
output.close()








