import pickle;
from person import Person;

f2 = open("person.ser","rb");

p1 = pickle.load(f2);

print(p1);
print(p1.name +"\n"+(str)(p1.age));
