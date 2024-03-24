
name = input("enter your name:")
age = input("enter your age:")
city = input("enter your city :")
number = input("enter your phone number:")

file = open('profile.txt',mode ='w')

file.write(f'my name is {name}')
file.write(f'i am  {age} years old')
file.write(f'i live in  {city}')
file.write(f'my phone number  is {number}')

file = open('profile.txt',mode='r')
print(file.readline())

file.close