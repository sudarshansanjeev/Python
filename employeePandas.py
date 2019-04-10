import numpy as py;
import pandas as pd;

df = pd.read_csv(r'C:\Users\768936\Desktop\CTS\Python\employeeDetails.csv',names=["id","name","age","salary","designation","department","project_id","project_name","manager","city","state"]);

#print(df);

# eldest
mx = df['age'].max();
#print(df[df.age==mx]);

# youngest
mn = df['age'].min();
#print(df[df.age==mn]);

# 2nd highest
hiPaid = (df.nlargest(2,'salary'));
#print(hiPaid);

# cost dep wise
depts = list(df['department'].unique());
for dep in depts:
    cost_dept_wise = df.groupby('department')['salary'].sum()[dep]
    #print(dep+" : "+(str)(cost_dept_wise));

#cost project wise
print("----Cost : project wise----");
projects =list(df['project_name'].unique());
for pro in projects:
    cost_pro_wise = df.groupby('project_name')['salary'].sum()[pro]
    #print(pro+" : "+(str)(cost_pro_wise));

# employees based on manager
print("--employees based on manager--");
managers = list(df['manager'].unique());
grouped = df.groupby('manager');
for manager in grouped:
    #print (manager);
    pass;
    
print(df['designation']);
#fill na with default values
df['designation'] = df ['designation'].fillna("employee")
print(df['designation']);



