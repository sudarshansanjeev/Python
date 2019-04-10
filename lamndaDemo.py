def abc(x):
    return x*x;

xyz = lambda y : y*y;

add = lambda x,y : x+y;
demo = add;

res = abc(10);
print(res);
res = xyz(5);
print(res);
res = add(10,20);
print(res );
res = demo(10,24);
print(res);

def div5():
    if(n%5==0):
        return True;
        
numbers = [ 22, 33 , 44 , 11, 665, 88, 4,5,210, 24,195,80];

res = list(filter(lambda n : n%5==0,numbers));

print(res);
print(numbers);
half = list(map(lambda n : n//3 , numbers));
print(half);

def somefunction(n):
    if(n==1):
        return lambda i : i * i;
    else :
        return lambda i : i * i * i;

functn = somefunction(2);
print(functn(4));

res = list(filter(lambda n:n%5, list(map(lambda n:n*2, numbers))))
print(res);
