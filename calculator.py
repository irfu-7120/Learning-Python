print ("Welcome to calculator")
print("input two numbers, enter the desired arithmetic operation, and this will give you the answer real fast")
x=str(input("type Y to Proceed/N To Terminate"))
if x=="Y":
   while True:
         
         a= int(input("enter number 1"))
         b= int(input("enter number 2"))
         print("type 1 if you want to add")
         print("type 2 if you want to subtract")
         print("type 3 if you want to multiply")
         print("type 4 if you want to divide")
         print("type 0 to close calculator")
         z= int(input("what operation do u wanna go with"))
         match z:
               case 0:
                    print("closing calculator...")
                    break
               case 1:
                    print("the sum is:",a+b)
               case 2:
                    print("the difference is:",a-b)
               case 3:
                    print("the product is:",a*b)
               case 4:
                    print("the output is:",a/b)
               case _:
                    print("invaild, lets try a different number")
   
elif x=="N":
     print("program terminated...")
     
else:
    print("invalid input bruh, prgrm terminating anyway")
          
         
   
   


