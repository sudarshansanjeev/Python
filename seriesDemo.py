import pandas as pd;
import numpy as np;

data = np.array(['Subhash','Ravi','Suman','Pratap','Shobha']);
s = pd.Series(data , index = [101,102,103,104,105]);

print(s);
print("------------------");

s = pd.Series('hello', index = [101,102,103,104,105]);
print(s);
print("---------------------");

s = pd.Series(['Geeta', 'Seeta','Rita','Meeta','Parineeta'],
              index = ['geet','s','r','m','pari']);

print(s[1]);
print(s['r']);
print(s['pari']);
