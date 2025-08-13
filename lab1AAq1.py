#You are required to compare the running time of the following two functions. Execute the
#program with different values of num and see how the running time changes for each of the
#functions. What do you notice?

import time

def linear_algo(num):
    for i in range(num):
        print(end="")

def quadratic_algo(num):
    for i in range(num):
        for j in range(num):
            print(end="")

num=100
start=time.time()
linear_algo(num)
print("linear time: ",time.time() - start)

start=time.time()
quadratic_algo(num)
print("quadratic time: ",time.time() - start)


#| num  | Linear Time (O(n))   | Quadratic Time (O(n²)) |
#| ---- | -------------------- | ---------------------- |
#| 100  | Very fast (\~0.000s) | Slightly slower        |
#| 1000 | Small increase       | Much slower            |
#| 5000 | Noticeable increase  | Extremely slow         |
