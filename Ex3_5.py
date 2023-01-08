def Marathon(distance):
 """

This function takes a list of integers and then converts all the numbers to the positive of that number
 and then adds them all together and returns "true" if the answer is 25 and "false" otherwise.
 Return False if the arguments are empty or not provided.

 Examples
Marathon( [1, 2, 3, 4] ) ➞ False
Marathon( [1, 9, 5, 8, 2] ) ➞ True
Marathon( [-6, 15, 4] ) ➞ True
 """
 x=[]
 i = 0
 for i in distance:
    
    if i<=0:
        a=i*(-1)
        x.append(a)
    else:
        x.append(i)
 sum=0
 for b in x:
    sum=sum+b
    if sum==25:
       return print("The distance is correct")
    else:
     return print("The distance is incorrect")

distanc=input(list)
print(Marathon(distanc))
