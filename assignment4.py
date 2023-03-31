#WAP using recursive function
def Recur_facto(n):
   
    if (n == 0):
        return 1
   
    return n * Recur_facto(n-1)
   
# print the result
print(Recur_facto(6))

#WAP to FILE handling

#Reading Mode
f = open("abhi.txt","r")
data=f.read()
print(data)

#writing mode\

f = open("abhi.txt","w")
data = f.write("All is well")
print(data)

#append Mode

with open("abhi.txt",'a') as file :
    f.write("every is fine ")



#function
def add_numbers(x=5, y=6):
    result = x + y
    return result

print(add_numbers())

#lambda function
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#lambda function into another function

def filter_even_numbers(numbers):
    # Use lambda function to filter even numbers
    even_numbers = filter(lambda x: x % 2 == 0, numbers) #filter() is used to make a list of even number
    return list(even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_even_numbers(numbers)
print(result)