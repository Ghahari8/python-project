#Multi-division 
def mul(a,b,c):

 i=0

 while i<b:
        a=a+a
        i=i+1
 
 

 if a%c==0:
    print("true")
 else:
    print("false")
    





a=int(input("please enter a:"))
b=int(input("please enter b"))
c=int(input("please enter c"))
print(mul(a,b,c))

