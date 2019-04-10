from flask import Flask, jsonify, request;
import pickle;
import os;
##class Employee:
##    def __init__(self,desig,salary):
##        self.desig=desig;
##        self.salary = salary;
####        print("\nEnter Details of "+self.desig);
####        self.name = input("Enter name : ");
####        self.age = input("Enter age : ");
        
class Clerk:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        self.salary = 15000;
        self.desig = "Clerk";
    def raiseSalary(self):
        self.salary = self.salary+3000;
                
class Programmer:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        self.salary = 30000;
        self.desig = "Programmer";
    def raiseSalary(self):
        self.salary = self.salary+5000;
                
class Manager:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        self.salary = 45000;
        self.desig = "Manager";
    def raiseSalary(self):
        self.salary = self.salary+10000;
        
class EmpDuck:
    def raiseEmployeeSalary(obj):
        obj.raiseSalary();
        
app = Flask(__name__);

##@app.route("/create/<string:name>/<int:age>/<int:choice>/", methods = ['POST'] )
##def create():
##    f1 = open("employee.ser","wb");
##    if choice==1:
##        emp = Clerk(name,age);
##    elif choice==2:
##        emp = Programmer(name,age);
##    elif choice==3:
##        emp = Manager(name,age);
##    pickle.dump(emp,f1);
##    f1.close();
##    return jsonify({"Result":"new Employee Created" });
           
@app.route("/display/", methods = ['GET' ] )
def display():
    f1 = open("employee.ser","rb");
    employeeList = pickle.load(f1);
    elist=[];
    #pickle.dump(employee,f1);
    print("displaying Employee details.....");
    for emp in employeeList :
        elist.append({'name':emp.name,'age':emp.age,});
        print("\nName : "+emp.name);
        print("\nAge : "+(str)(emp.age));
        print("\nSalary : "+(str)(emp.salary));
        print("\nDesignation : ",emp.desig);
    f1.close();
    return jsonify(elist);

@app.route("/raise-salary/",methods = ['GET','POST'] )
def raiseSalary():
    f1 = open("employee.ser","rb");
    employeeList = pickle.load(f1);
    f1.close();
    for emp in employeeList :
        print(emp);
        EmpDuck.raiseEmployeeSalary(emp);
    
    f2 = open("employee.ser","wb");
    pickle.dump(employeeList,f2);
    f2.close();
    return jsonify({"Result":"Salary Raised..."});         

@app.route("/check-file/",methods = ['GET'])
def checkFile():
    if(not(os.path.exists("employeeList.ser"))):
        f1 = open("employee.ser","wb");
        employeeList = []
        pickle.dump(employeeList,f2);
        f1.close();
    return jsonify({"":"Welcome to Employee Management App"});

if __name__ == '__main__':
    app.run(debug=True);

