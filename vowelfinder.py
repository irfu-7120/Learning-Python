print("Welcome, this will find you the number of Text/vowels.... in any word/sentence you have got")
print("But Before Any Of That Happens....")
passs =str(input("Enter The Password For Access:"))
if passs =="irfu":
   while True:
         print("Type 0 to terminate")
         Word=str(input("Enter any word:"))
         number=0
         aa=0
         ee=0
         ii=0
         oo=0
         uu=0 
         total=0
         if Word=="0":
                print("okayy... terminating now")
                break
         for vowel in Word:
             if vowel==("e"):
                     number=number+1
                     ee=ee+1
             if vowel==("a"):
                     number=number+1
                     aa=aa+1
             if vowel==("i"):
                     number=number+1
                     ii=ii+1
             if vowel==("o"):
                     number=number+1
                     oo=oo+1
             if vowel==("u"):
                     number=number+1
                     uu=uu+1
             total=total+1
         print("Total Number of Text Found:",total)
         print("number of vowels found:",number)
         print("a's:",aa)
         print("e's:",ee)
         print("i's:",ii)
         print("o's:",oo)
         print("u's:",uu)

else: 
     print("INCORRECT PASSWORD")
     print("Honeslty FUCK U")

    
