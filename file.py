#f1 = open("abc.txt", "r");

#print(f1.read());

#print(f1.readline() , end="");
#print(f1.readline() , end="");
#print(f1.readline() , end="");
#print(f1.readline() , end="");

#f1.close();
##
###f2 = open("xyz.txt", "w");
##f2.write("Writing content through python...");
##f2.write("\nsome more content...")
##f2.write("\nJust for demo");
##f2.close();

##f2 = open("xyz.txt", "a");
##
##for data in f1 :
##    f2.write(data);
##f2.close();

##f3 = open("bankbg.jpg", "rb");
##
##f4 = open("copy.png", "wb");
##for data in f3:
##    f4.write(data);
##f4.close();

f5 = open("C://Users//768936//Desktop//CTS//Python//xyz.txt","r");
f5.seek();
print(f5.read());
