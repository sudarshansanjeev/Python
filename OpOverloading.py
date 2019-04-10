class Emp:
    def __init__(self, name,age, salary) :
        self.name = name;
        self.salary = salary;
        self.age = age;
    def __str__(self):
        print("Name : ",self.name);
        print("Salary : ",self.salary);
        return " ";
    def __add__(obj1, obj2):
        x = obj1.salary;
        y = obj2.salary;
        z = x+y;
        e = Emp("Verma Family",12,z);
        return e;
    def __gt__(obj1,obj2):
        x = obj1.age;
        y = obj2.age;
        if(x>y):
            return obj1;
        else:
            return obj2;
    
        
         
e1 = Emp("Ravi Verma",34,32000);
e2 = Emp("Sushi Verma",43,45000);

e4 = e1+e2;
print(e4);
print(e1>e2);

 
