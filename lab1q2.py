#Implement a program that reads a positive integer value, num, and calculates and displays
#the sum of all prime numbers from 1 up to and including num.
#A prime number is an integer greater than 1 that cannot be exactly divided by any integer
#other than 1 and itself. Some examples of prime numbers are 2, 3, 5, 7, and 11.

value= 0
psum=0 

print("enter a positive integer")
value=int(input())

while value < 0:
 print("enter a positive integer")
 value=int(input())

print()
print("You entered:", value) #identation important in python dont forget to remove space to end loop

for i in range(2, value + 1):
    is_prime = True  
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break 
    
    if is_prime:
        print(i, "is a prime number")
        psum += i

print("sum of all prime numbers up to and including the number is : ",psum)




