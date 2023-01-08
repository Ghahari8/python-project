def ex3_6(faceinterval):

 max1=max(faceinterval)
 min1=min(faceinterval)
 x=(max1)-(min1)

 for i in faceinterval:
    if i==x:
        print(":)")
    elif i!=x:
        print(":(")
    elif (len(faceinterval==0)):
        print(":/")