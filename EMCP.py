n1 = input ("What is number 1")
n2 = input ("What is number 2")
n3 = input ("What is number 3")

if n1 >n2:
    if n1>n3:
        print ("number 1 is the biggest one")
if n2 > n3:
    if n2 > n1:
        print ("number 2 is bigger than all of them")
else:
    if n3>n2:
        if n3>n1:
            print ("number 3 is bigger than all of them")
