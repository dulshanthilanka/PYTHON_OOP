list = [32,75,39,59,92]
print(list)
a = len(list)
for i in range(a):
    for j in range(a-1):
        if list[j]>list[j+1]:
            temp = list[j]
            list[j]=list[j+1]
            list[j+1]=temp
            
print(list)