
class Dog:
    # Class attribute
    species = "Canis lupus familiaris"
    
    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."

# Creating an object (instance of the class)
dog1 = Dog("Buddy", 3)
print(dog1.description())  # Output: Buddy is 3 years old.
print(dog1.speak("Woof!"))  # Output: Buddy says Woof!


fork = Dog("fork", 5)
print(fork.description()) 
print(dog1.speak("Woof!"))

dogs =[dog1,fork]
from functools import reduce
import sys
ages_sum = reduce((lambda s,dog: s + dog.age), dogs,0)
print(ages_sum)

nums=[10,20,30,40]
nums_sum=reduce(lambda s, num:s+num,nums,0)
nums_pr=reduce(lambda q, num: q * num,nums ,1)
print(nums_sum,nums_pr)

min_num=reduce(lambda m,num:min(m,num),nums,sys.maxsize)
max_num=reduce(lambda m,num:max(m,num),nums,-sys.maxsize)

print(min_num,max_num)

nums_min = reduce(min,nums)
nums_max=reduce(max,nums)
print(nums_max,nums_min)
