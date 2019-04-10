import pandas as pd;
import numpy as np;

df = pd.read_csv(r'C:\Users\768936\Desktop\CTS\Python\pandas_demo_data.csv',delimiter=";",names=['date_time','read_write','country','user_id','d_market','contintent']);
#print(df);
print(df.head(3));
print(df.tail(4));

print(df[df.d_market=="SEO"]);

#print(df.head()[['country', 'continent', 'user_id']]);

print(df.sample(5)[['country', 'contintent', 'user_id']]);
