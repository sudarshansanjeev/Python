
y=1;

def abc() :
    x = 1;
    print("x value : ",x);
    x+=1;

def xyz() :
    global y; 
    print("y value : ",y);
    y+=1;

abc();
abc();

xyz();
xyz();
