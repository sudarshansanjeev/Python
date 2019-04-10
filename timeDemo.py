import time;
import calendar;
ms = time.time();

print("Milliseconds : ",ms);
print("Time : ",time.localtime(ms));
print("Meaningful Time : ", time.asctime(time.localtime(ms)));


print("-------------------");
cal = calendar.month(2019,3,3);
print(cal);

print("-------------------");
str = "Lowercase...";
print(str);
print(str.lower());

