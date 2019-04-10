from numpy import *;

arr = array([1,2,3,4,5.0], str);
print(arr);

print(arr.dtype);
print(type(arr));

ls = linspace(1, 50, 12);
print(ls);

logs = logspace(1,41,42);
print(logs);
print("%.1f"%logs[3]);


ar = arange(50, 1, -12);
print(ar);

z1 = zeros(5);
print(z1);
z2 = zeros(5,str);
print(z2);

z3 = zeros(5,int);
print(z3);

z4 = zeros(5,int);
print(z4);

o1 = ones(5);
print(o1);

o2 = ones(5,int);
print(o2);

o3 = ones(5, str);
print(o3);
o4 = ones(5,bool);
print(o4);





