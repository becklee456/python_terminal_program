# pyhton generators

# def count_up_to(n):
#     count=1
#     while count<=n:
#         yield count
#         count+=1

# for number in count_up_to(5):
#     print(number)

# closures

# def parent(name):
#     def child():
#        print(name)
#     return child    

# names=parent("becken")    
# names()

# def decorator_func (inner_func):
#     def wrapper():
#         print("wrapper executed before {}".format(inner_func.__name__))
#         return inner_func
#     return wrapper  

# @decorator_func
# def display():
#     print("hello")


# display()  


# def apply_function(func,value):
#     return func(value)

# def square(x):
#     return x*x

# h_o=apply_function(square,3)

# print(h_o)