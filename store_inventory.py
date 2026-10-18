print("Welcome To Store Inventory Manager")
print ("Find/List?Add or Delete ITEMS from Your Store Inventory")
passs=str(input("enter store name to access your inventory"))   #the password is sam store
store_inventory= [ "milk", "bread", "eggs","Cocoa Powder", "Maggie Instant Noodles", "Chaat Masala"]
if passs=="sam store":      
   while True:
         
         print ("Enter 1 for listing All The Items In the Inventory")
         print ("Enter 2 To Find If Any Item is present in the List Or Not")
         print ("Enter 3 to Add Any New Items To The List")
         print ("Enter 4 To Delete Any Item From the List")
         print ("Enter 0 To Exit The Program")
         x= int(input("So What Do u wanna do?:"))
         innum=0
         num=0
         match x:
               case 1:
                    for items in (store_inventory):
                                  innum=innum+1
                    print("Total Number Of Item Found:",innum)
                    for items in (store_inventory):
                                  num=num+1   
                                  print(num,items)
                    
                       
               case 2:
                    searc=str(input("Alright Type The Name Of The Item You Wanna Find:"))
                    if searc in (store_inventory): 
                               print ("In Stock")
                    else:
                        print("Out Of Stock")
               case 3:
                    newt=str(input("type the item you wanna log:")) #for entering multiple items, seperate with commas
                    addeditems=newt.split(",")
                    for item in addeditems:
                         cleanitems=item.strip()
                         store_inventory.append(cleanitems)
                         print ("Item",cleanitems,"Added")
               case 4:
                    delt=str(input("type the item you wanna remove:"))
                    if delt in store_inventory:
                             store_inventory.remove(delt)
                             print("item", delt, "removed")
                    else:
                        print("That item isn't in the inventory, so it can't be removed.")
               case 0:
                    print("exiting the program....")
                    break
               case _:
                    print ("invalid input try again")
                   


else:
   print("wrong password,access denied")
   
         
