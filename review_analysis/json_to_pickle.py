import pickle
import string
from string import maketrans
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

data={}
jj=0
intab = string.punctuation
outtab = "                                "
trantab = maketrans(intab, outtab)

sw=stopwords.words("english")
stemmer=SnowballStemmer("english")

with open('electronics.json') as jsonf:
    for i in jsonf:
        str1=eval(i)['reviewText']
        str1 = str1.translate(trantab)
        words=str1.split(" ")

        dict1 = {}
        c = 0
        co=0
        max=-1
        max2=-1
        for j in words:
            if j not in ["", " "] + sw:
                c += 1
                keys = dict1.keys()
                k = str(stemmer.stem(j))
                if k in keys:
                    dict1[k][0] = (float(dict1[k][0])*dict1[k][1]+float(c))/float(dict1[k][1]+1)  # at 0= sum of pos, at 1= frequency
                    if dict1[k][0]>max:
                        max=dict1[k][0]
                    dict1[k][1] += 1.0
                    if dict1[k][1]>max2:
                        max2=dict1[k][1]
                else:
                    co+=1
                    temp = {}
                    temp[0] = float(c)
                    temp[1] = 1.0
                    dict1[k] = temp
                    if dict1[k][0]>max:
                        max=dict1[k][0]
                    if dict1[k][1]>max2:
                        max2=dict1[k][1]

        if co>=10:
            keys=dict1.keys()
            for j in keys:
                dict1[j][0]/= max
                dict1[j][1] /= max2

            data[eval(i)['reviewerID']]=dict1
        jj+=1
        #print data[eval(i)['reviewerID']]
        if(jj%1000==0):
            print jj


output=open('reviews.pkl','wb')
pickle.dump(data,output)
output.close()