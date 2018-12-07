#Lab 10

#1. Type the following lambda functions
f=lambda x, y: x+y
g=lambda x, y: x*y
h=lambda x, y: x**y
#What are f(1,1), and f(2,3)?
f(1,1) = 2; f(2,3) = 5
#What are g(1,1), and g(2,3)?
g(1,1) = 1; g(2,3) = 6
#What are h(1,1), and h(2,3)?
h(1,1) = 1; h(2,3) = 8
#What values are x and y when f = g =h? Hint: Try negative numbers. Try zero.
f=lambda x, y: x+y
g=lambda x, y: x*y
h=lambda x, y: x**y
f=g=h
print(f(-1,-2))
#Output: 1; x = -1, y = -2
print(f(-2,0))
#Output: 1; x = -2, y = 0


#2. Write a lambda function such that
# f(x) is x itself
f=lambda x: x
print(f(1))
#Output: 1

# f(x) is the abs(x)
f=lambda x: abs(x)
print(f(-5))
#Output: 5
#Make sure you test your outputs


#3. Write a map function to map a list of numbers into the absolute version of the numbers
#For example, after the map function is used, this list [1,-2,-4,5,-6,-15] becomes [1,2,4,5,6,15]
x = [1,-2,-4,5,-6,-15]
y = [abs(i) for i in x]
print(y)
