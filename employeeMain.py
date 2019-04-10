import pickle;
import os;
class Employee:
    def __init__(self,desig,salary):
        self.desig=desig;
        self.salary = salary;
        print("\nEnter Details of "+self.desig);
        self.name = input("Enter name : ");
        self.age = input("Enter age : ");
        

class Clerk(Employee):
    def __init__(self):
        super().__init__("Clerk",15000);
    def raiseSalary(self):
        self.salary = self.salary+3000;
                
class Programmer(Employee):
    def __init__(self):
        super().__init__("Programmer",35000);
    def raiseSalary(self):
        self.salary = self.salary+5000;
                
class Manager(Employee):
    def __init__(self):
        super().__init__("Manager",50000);
    def raiseSalary(self):
        self.salary = self.salary+10000;

class EmpDuck:
    def raiseEmployeeSalary(obj):
        obj.raiseSalary();


def create():
    print("-------------------");
    print("1. Clerk");
    print("2. Programmer");
    print("3. Manager");
    print("4. exit");
    choice = int(input());

    if choice==1:
        employeeList.append(Clerk());
    elif choice==2:
        employeeList.append(Programmer());
    elif choice==3:
        employeeList.append(Manager());
    else:
        print("Please enter valid choice...");

def display():
##    f1 = open("employee.txt","r");
##    for data in f1 :
##        arr = data.split(" | ");
##        print("Name : "+arr[0]+"\nAge : "+arr[1]+"\nSalary : "+arr[2]+"\nDesignation : "+arr[3]);
##       
##    f1.close();
    print("displaying Employee details.....");
    for emp in employeeList :
        print("\nName : "+emp.name);
        print("\nAge : "+(str)(emp.age));
        print("\nSalary : "+(str)(emp.salary));
        print("\nDesignation : ",emp.desig);

def raiseAllSalary() :
    for emp in employeeList :
        print(emp);
        EmpDuck.raiseEmployeeSalary(emp);
    
if(os.path.exists("employee.ser")):
    f1 = open("employee.ser","rb");
    employeeList = pickle.load(f1);
    f1.close();
else:
    employeeList = []
count=0;
while(True):
    
    print("\n------------------------");
    choice = int(input("1.Create \n2.Display \n3.RaiseSalary \n4.Exit\n"));
    print("------------------------")
    if choice == 1:
        create();
    elif choice == 2:
        display();
    elif choice == 3:
        raiseAllSalary();
    elif choice == 4:
        f2 = open("employee.ser","wb");
        pickle.dump(employeeList,f2);
        f2.close();
        print("Total number of employees added ",count);
        break;

    
    
