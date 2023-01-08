#Robot Path
def robot(direction):

 """
We have a robot that moves in four geographical directions and has two specified destinations.
By giving a list of directions, the code checks whether the robot reaches the specified destination or not.

Destination No. 1: e, n, e, e, n
Destination No. 2: w, n, w, n, w, w, n

examples:
robot( ["s", "e", "e", "n", "n", "e", ”n"] ) ➞ True
# Robot will end up at robot no. 1

robot( ["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", ”e"] ) ➞ False
# Robot will be lost somewhere

robot( ["n", "s", "n", "n", "e", "n", "w", "w", "s", "w", "w", "w", ”n"] ) ➞ True

"""
 x=0
 y=0
 for directs in direction:
    if directs=="e":
      x=x+1
    elif directs=="w":
        x=x-1
    elif directs=="n":
        y=y+1
    elif directs=="s":
    
        y=y-1
 if x==3 and y==2 or x==-4 and y==3 :
  return True  

 else:
    return False
x=input(list)
print(robot(x))