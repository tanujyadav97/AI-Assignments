import pickle
import operator
file=open("result.pkl","r")
data=pickle.load(file)
sorted_x = sorted(data.items(), key=operator.itemgetter(1))
sorted_x.reverse()
print("Customer id     Score(out of 10)")
for i in sorted_x:
    print(i)