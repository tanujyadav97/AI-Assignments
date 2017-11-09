import string
from string import maketrans
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from scipy.stats import pearsonr

with open('1.txt', 'r') as f:
  str1=f.read()

with open('2.txt', 'r') as f:
  str2=f.read()

intab = string.punctuation
outtab = "                                "
trantab = maketrans(intab, outtab)

str1=str1.translate(trantab)
str2=str2.translate(trantab)

words1=str1.split(" ")
words2=str2.split(" ")

sw=stopwords.words("english")
stemmer=SnowballStemmer("english")

dict1={}
c=0
for i in words1:
    if i not in [""," "]+sw:
        c+=1
        keys=dict1.keys()
        j=str(stemmer.stem(i))
        if j in keys:
            dict1[j][0]+=float(c)                    # at 0= sum of pos, at 1= frequency
            dict1[j][1]+=1
        else:
            temp={}
            temp[0]=float(c)
            temp[1]=1
            dict1[j]= temp

dict2={}
c=0
for i in words2:
    if i not in [""," "]+sw:
        c+=1
        keys=dict2.keys()
        j=str(stemmer.stem(i))
        if j in keys:
            dict2[j][0]+=float(c)                    # at 0= sum of pos, at 1= frequency
            dict2[j][1]+=1
        else:
            temp={}
            temp[0]=float(c)
            temp[1]=1
            dict2[j]= temp


keys1=dict1.keys()
keys2=dict2.keys()

list1=[]
list2=[]

for i in keys1:
    if i in keys2:
        list1.append(dict1[i])
        list2.append(dict2[i])
    else:
        list1.append(dict1[i])
        temp={}
        temp[0]=0.0
        temp[1]=0
        list2.append(temp)

for i in keys2:
    if i not in keys1:
        list2.append(dict2[i])
        temp={}
        temp[0]=0.0
        temp[1]=0
        list1.append(temp)

c=0
for i,j in zip(list1,list2):
    if list1[c][1]!=0:
        list1[c][0]/=float(list1[c][1])
    if list2[c][1]!=0:
        list2[c][0]/=float(list2[c][1])

pos1=[]
pos2=[]

max1=-1.0
max2=-1.0

for i,j in zip(list1,list2):
    pos1.append(float(i[0]))
    pos2.append(float( j[0]))
    if(i[0]>max1):
        max1=i[0]
    if(j[0]>max2):
        max2=j[0]

c=0
for i,j in zip(pos1,pos2):
    pos1[c]=i/max1
    pos2[c]=j/max2
    c+=1


similirity1=pearsonr(pos1,pos2)

freq1=[]
freq2=[]

max1=-1.0
max2=-1.0

for i,j in zip(list1,list2):
    freq1.append(float(i[1]))
    freq2.append(float( j[1]))
    if(i[1]>max1):
        max1=i[1]
    if(j[1]>max2):
        max2=j[1]

c=0
for i,j in zip(freq1,freq2):
    freq1[c]=i/max1
    freq2[c]=j/max2
    c+=1


similirity2=pearsonr(freq1,freq2)


print "Similarity is ", (abs(similirity1[0])+abs(similirity2[0]))*50,"%"