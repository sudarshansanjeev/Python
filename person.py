class Person:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

    def __str__(self):
        print("Name : ",self.name);
        print("Age : ",self.age);
        return "";
