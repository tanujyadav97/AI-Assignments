import pandas as pd
import pickle

#  SORTED THE FILE WITH CUSTOMER ID SO THAT THEIR MOST RECENT PURCHASE IS AT THE TOP

file = 'Online Retail.xlsx'
xl = pd.ExcelFile(file)
df1 = xl.parse('Online Retail')



data={}
y=0
temp={}
for i in df1['CustomerID']:
    temp[i]=0
    y+=1
    if y==406829:
        break
y=0
for i in df1['CustomerID']:
    if temp[i]==0:
        rowd={}
        data[i]=rowd
        temp[i]=1


    cus=[]
    if df1['Quantity'][y]>0:
        cus.append(df1['Quantity'][y]*df1['UnitPrice'][y])
        cus.append(str(df1['InvoiceDate'][y]).split(' ')[0].split('-')[0])
        cus.append(str(df1['InvoiceDate'][y]).split(' ')[0].split('-')[1])
        cus.append(str(df1['InvoiceDate'][y]).split(' ')[0].split('-')[2])
        data[i][len(data[i])]=cus

    y+=1
    if y==406829:
        break


data1={}
y=0
key=data.keys()
for cus in data:
    data1[key[y]]={}
    yy=0
    mm=0
    dd=0
    sum=-1
    for pur in data[cus]:

        if (data[cus][pur][1]==yy)&(data[cus][pur][2]==mm)&(data[cus][pur][3]==dd):
                sum+=data[cus][pur][0]
        else:
            if sum>-1:
                ls=[]
                ls.append(sum)
                ls.append(yy)
                ls.append(mm)
                ls.append(dd)
                data1[key[y]][len(data1[key[y]])]=ls
                sum=data[cus][pur][0]
                yy=data[cus][pur][1]
                mm=data[cus][pur][2]
                dd=data[cus][pur][3]
            else:
                sum = data[cus][pur][0]
                yy = data[cus][pur][1]
                mm = data[cus][pur][2]
                dd = data[cus][pur][3]
    ls = []
    ls.append(sum)
    ls.append(yy)
    ls.append(mm)
    ls.append(dd)
    data1[key[y]][len(data1[key[y]])] = ls
    y+=1


y=0
key=data1.keys()
data2={}
max1=-1
for cus in data1:
    score=0
    u=2011*12+12-int(data1[cus][0][1])*12-int(data1[cus][0][2])
    score+=max(1,min(10,10-u))                              #recency
    c=0
    maxx=-1
    for pu in data1[cus]:
       if(2011*12+12-int(data1[cus][pu][1])*12-int(data1[cus][pu][2])<=12):
           c+=1
       if data1[cus][pu][0]>maxx:
            maxx=data1[cus][pu][0]

    if maxx>max1:
        max1=maxx

    score+=max(1,min(10,c))                              #frequency
    data2[key[y]]=[]
    data2[key[y]].append(score)
    data2[key[y]].append(maxx)

    y+=1



y=0
data3={}
key=data2.keys()
for cus in data2:
    data3[key[y]]=(data2[key[y]][0]+(data2[key[y]][1]/max1)*10)/3
    y+=1

output=open('result.pkl','wb')
pickle.dump(data3,output)
output.close()


