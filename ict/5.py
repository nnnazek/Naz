a = int(input("How many bottles have one litre or less: ")) 
b = int(input("How many bottles have more than one litre: ")) 
 
c = (a * 0.10) + (b * 0.25) 
 
print("The c for returning these containers is ${0:.2f}.".format(c))