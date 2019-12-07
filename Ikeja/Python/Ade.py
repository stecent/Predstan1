print("Welcome to the Area Calculator Designed By Raji")
print("1. Triangle \n 2. Square \n 3. Circle")
while True:
 ShapeNumber = input("Please Enter Shape Number")
 try: 
  ShapeNumber = int(ShapeNumber)
  break   
 except:
  print("Please Enter either 1, 2 or 3")
while True:
 ShapeNumber = int(input("Pleaee ReEnter shape Number"))
 if ShapeNumber == 1:
    	print ("Area of a Triangle")
    	Base= int(input("Enter the Base of the Triangle"))
    	Height= int(input("Enter the Height of the Triangle"))
    	ATriangle = 1/2*Base*Height
    	print("The area of the Triangle is:" ,ATriangle)
    	break
 elif ShapeNumber ==2:
    print("Area of a Square")
    Length = int(input("Enter the length of one side of the Square"))
    ASquare = 2*Length 
    print("Area of the Square is: ", ASquare)
    break
 elif ShapeNumber ==3:
    print("Area of a Circle")
    import math
    r=int(input("Please Enter Radius of the Circle"))
    ACircle=r*r*math.pi
    ACircle = round(ACircle, 2)
    print("Area of the circle is:", ACircle)
    break
 else:
    print("You Must either Choose 1, 2 or 3")
    continue 
     
