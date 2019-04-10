def abc(a, b):
    print("a : ",a);
    print("b : ",b);

def xyz(name, age , salary , designation):
    print("name : ",name);
    print("age : ",age);
    print("salary : ",salary);
    print("designation : ",designation);
    
def opt(name, age , salary , designation="employee"):
    print("name : ",name);
    print("age : ",age);
    print("salary : ",salary);
    print("designation : ",designation);

def add(*a):
    result = 0;
    for i in a:
        print(i);
        result=result+int(i);
    print("result : ",result);

abc(12,45);

print("----------------------------");

xyz(name = "sanjeev", age = 23, salary = 4509909, designation = "programmer")  # keyword function

print("-----------------------------");

opt("raja",43,234234);

print("-----------------------------");

add(18,64);

print("-----------------------------");

add(43,99,100);

#abc(12,23,45);

