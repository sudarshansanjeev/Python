import pandas as pd;

weather_data = {
    'day': ['1/3/2019','2/3/2019','3/3/2019','4/3/2019','5/3/2019','6/3/2019','7/3/2019','8/3/2019'],
    'temperature': [25,32,29,35,33,26,28,24],
    'windspeed': [3,4,5,9,6,2,4,5],
    'event' : ['sunny','rainy','snowy','spring','sunny','snowy','rainy','sunny']
    }

df = pd.DataFrame(weather_data);
print(df);
print(df.shape);

rows, columns = df.shape;
print("Rows : ",rows);
print("Columns : ",columns);
#print(df.head());
#print(df.head()[['day','windspeed']]);
print(df.max()[['temperature']]);
print(df.min()[['temperature']]);
print(df.mean()[['temperature']]);

      


