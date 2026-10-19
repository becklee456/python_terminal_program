# from collections import deque


# dq=deque()

# dq.append("A")
# dq.append("b")
# dq.append("c")
# dq.append("f")
# dq.appendleft("w")
# dq.remove(dq[0])

# print(dq)


# import os

# file="exaple"

# square = [x * 2 for x in range(10)]
# print(square)
# def generate_numbers(n): 
#     for i in range(n): 
#         yield i*2
 
# # Using the generator 
# for number in generate_numbers(10): 
#     print(number)

# try: 
#     result = 10 / 0 
# except ZeroDivisionError: 
#     print("You cannot divide by zero.") 
# import unittest 
 
# def add(a, b): 
#     return a + b 
 
# class TestMathFunctions(unittest.TestCase): 
#     def test_add(self): 
#         self.assertEqual(add(1, 2), 3) 
 
# if __name__ == "__main__": 
#     unittest.main() 

# newList=[1,2,3,4,5,6,6,7] 
# newList.append(5)
# print(newList)

# x = 20 
# if x < 10: 
#  print("Small") 
# else: 
#  print("Large") 

# def sum(x , y):
#     return x + y
# print(f"sum is: {sum(3 , 4)}")

# def multiplication(x , y):
#     return x * y

# print(f"multiplication {multiplication(3 , 4)}")

# def division(x , y):
#     return x / y
# print(f"division is: {division(3 , 4)}")


# def exponential(x , y):
#     return x ** y
# print(f"exponential is: {exponential(3 , 4)}")


# def substraction(x , y):
#     return x - y
# print(f"substraction is: {substraction(3 , 4)}")

#!hello

def numbers () :
    yield 1
    yield 2
    yield 3
    yield 4

for num in numbers ()
      print (num)