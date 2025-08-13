#Implement a function reverse_string that takes a string as argument and returns the reverse
#of the latter, without using slicing. For example, reverse_string(“hello”) will return “olleh”.

#slicing aka string[start:stop:step]

Any_text=""

Any_text=str(input("enter a string "))

arraylist=list(Any_text)

print (arraylist)

lenList=len(arraylist)

print(lenList)



while lenList!=0:

    print(arraylist[lenList-1])
    lenList-=1

