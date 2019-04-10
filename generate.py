def abc():
    yeild 1;
    yeild 21;
    yeild 23;
    

collection = abc();

print(collection.__next());
print(collection.__next());
print(collection.__next());

for i in collection:
    print(i);

def cube():
    for i in range(1,11):
        num = i*i*i;
        yeild num;

cb = cube();

for i in cb:
    print(i);
