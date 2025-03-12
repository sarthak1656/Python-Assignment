oglist=["apple","cat","banana","kiwi"]
reslist=[]
n = 3

for i in oglist:
    if len(i)>n:
        reslist.append(i)
    
print(reslist)