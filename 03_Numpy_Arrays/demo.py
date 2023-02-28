# We cannot perform operations like multiplication, addition etc on whole list at once.
# a * 2 will concatenate the array twice.
# Therefore we have numpy arrays

a = [1, 2, 3, 4, 5]

# squares = []
# for i in a:
#     squares.append(i**2)

squares = [i**2 for i in a]
print(squares)

# sqaure only even numbers
squares = [i**2 for i in a if i%2==0]
print(squares)

import numpy as np

a  = [1, 2, 3, 4, 5, 6]
b = np.array(a);

print(b);

# shape is tuple for a numpy array
print(b.shape);

c = [[1, 2], [3, 4]]
b = np.array(c);
print(b);
print(b.shape);
print(type(b));

# b*2 when b is a numpy array multiplies every number by 2
print(b*2)

# Intilaising numpy array with zeroes and ones
a = np.zeros((2, ));
print(a)

a = np.ones((2, 2));
print(a)

# Intilaing with some other number
a = np.full((2, 2), 5);
print(a)

# Identiy matrix
a = np.eye(2);
print(a)

# Random values
a = np.random.random((2, 2))
print(a)


# slice
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]);
print(a);

# All rows second column
print(a[:,2])

# Row 1 and 2, column 0 and 1
print(a[1:3,0:2])

# Multiplication of arrays

x = np.array([[1, 2], [3 , 4]], dtype = np.float64)
y = np.array([[1, 2], [3 , 4]], dtype = np.float64)
print(np.multiply(x,y)) #pixel wise multiplication

print(x*y) #pixel wise multiplication

# Broadcasting
x  = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([2, 3, 4]);
# Each row will get added with x
print(x+y);