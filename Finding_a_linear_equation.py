print("Enter x1: ")
x1 = float(input())
print("Enter y1: ")
y1 = float(input())
print("Enter x2: ")
x2 = float(input())
print("Enter y2: ")
y2 = float(input())
piece = y1 - y2
piece2 = x2 - x1
piece3 = x1*y2 - x2*y1
dar1 = str(piece)
dar2 = str(piece2)
dar3 = str(piece3)
if(piece>0 and piece2>0 and piece3>0):
   print("Answer: " + dar1 + "x + " + dar2 + "y + " + dar3 + " = 0 ")
if(piece<0 and piece2<0 and piece3<0):
   print("Answer: " + dar1 + "x " + dar2 + "y " + dar3 + " = 0 ")
if(piece>0 and piece2>0 and piece3<0):
   print("Answer: " + dar1 + "x + " + dar2 + "y " + dar3 + " = 0 ")
if(piece>0 and piece2<0 and piece3<0):
   print("Answer: " + dar1 + "x " + dar2 + "y " + dar3 + " = 0 ")
if(piece<0 and piece2<0 and piece3>0):
   print("Answer: " + dar1 + "x " + dar2 + "y + " + dar3 + " = 0 ")
if(piece<0 and piece2>0 and piece3>0):
   print("Answer: " + dar1 + "x + " + dar2 + "y + " + dar3 + " = 0 ")
if(piece<0 and piece2>0 and piece3<0):
   print("Answer: " + dar1 + "x + " + dar2 + "y + " + dar3 + " = 0 ")
if(piece>0 and piece2<0 and piece3>0):
   print("Answer: " + dar1 + "x " + dar2 + "y + " + dar3 + " = 0 ")
if(piece3==0):
   print("Answer: " + dar1 + "x + " + dar2 + "y + " + dar3 + " = 0 ")
else:
    print("Incorrect values entered")