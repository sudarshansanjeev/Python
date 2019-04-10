import pickle;
import os;
import requests;
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
##    url = "http://localhost:5000/create/";
##    print("-------------------");
##    print("1. Clerk");
##    print("2. Programmer");
##    print("3. Manager");
##    print("4. exit");
##    choice = int(input());
##    if choice==1:
##        emp = Clerk();
##    elif choice==2:
##        emp = Programmer();
##    elif choice==3:
##        emp = Manager();
##    else:
##        print("Please enter valid choice...");
##    age = (str)(emp.age); choice1 = (str)(choice);
##    url = url + emp.name + "/" +age+ "/"+choice1 + "/";
##    result = requests.get(url).json();
    
        
def display():
    url = "http://localhost:5000/display/";
    print("Displaying....");
    result = requests.get(url).json();
    print(result);
def raiseAllSalary() :
    url = "http://localhost:5000/raise-salary/";
    result = requests.get(url).json();

if(not(os.path.exists("employeeList.ser"))):
        f1 = open("employeeList.ser","wb");
        employeeList = []
        pickle.dump(employeeList,f2);
        f1.close();
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
        break;

    
    
