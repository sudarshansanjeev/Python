from threading import *;
from time import *;
class A(Thread):
    def run(self):
        for i in range(1,21):
            print("i : ",i);
            sleep(1);

class B(Thread):
    def run(self):
        for j in range(1,21):
            print("j : ",j);
            sleep(1);

class C(Thread):
    def run(self):
        for k in range(1,21):
            print("k : ",k);
            sleep(1);

a1 = A();
b1 = B();
c1 = C();

a1.setDaemonThread(true);

a1.start();
b1.start();
c1.start();

print("a1 is alive ",a1.isAlive());
print("b1 is alive ",b1.isAlive());
print("c1 is alive ",c1.isAlive());
