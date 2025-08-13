#Suppose that you have to build a feature for a Maths learning application. Given a number,
#the application must be able to determine whether it is a perfect square. A perfect square is
#an integer that is the square of another integer (its square root is not a decimal value). E.g., 1,
#4, 9 and 16 are examples of perfect squares.
#(a) You are required to implement a function is_perfect_square that takes as argument an
#integer and returns True/False depending on whether the integer is a perfect square. For
#example, is_perfect_square(25) returns True while is_perfect_square(15) returns False.
#(b) You are required to define a function list_perfect_square that takes an integer value num
#and prints the first num perfect squares.

value=0
p_square=False

def is_perfect_square(n):
    
    if ((n**0.5)*(n**0.5))==n:
        p_square=True
    elif ((n**0.5)*(n**0.5)) !=n:
        p_square=False
    return p_square

#or use root then like root times root == n

def list_perfect_square(num):

    for i in range(1,num+1):
        print(i*i,end=" ")
        



value=int(input("enter a value "))
perfect=is_perfect_square(value)
print(perfect)
list_perfect_square(value)

