class cal:
    def _init_(self,a,b,c):
        self.a=a
        self.b=b
    def add(a,b,c):
        return a+b+c
    def sub(a,b):
       return a-b
    def div(a,b):
        return a/b
    def mult(a,b):
        return a*b
obj_1=cal
ch=int(input("enter your choice  "))
a=int(input("enter your value a"))
b=int(input("enter your value b"))
if(ch==1):
    print(obj_1.add(10,20))
elif(ch==2):
    print(obj_1.sub(10,20))
elif(ch==3):
    print(obj_1.div(10,20))
else:
    print(obj_1.mult(10,20))
