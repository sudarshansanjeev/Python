x = 10;
y = 20;

print(id(x));
print(id(y));

y = x;

print(str(id(x))+" "+str(id(y)));
