import math;
arr = [];
for i in range(5):
    arr.append(int(input("Enter "+str(i)+"value : ")));

for i in arr:
    sq= math.sqrt(i);
    if(math.ceil(sq)==sq):
        print(i);
        
       
