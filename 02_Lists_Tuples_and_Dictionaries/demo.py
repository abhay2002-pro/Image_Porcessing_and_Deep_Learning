
# ---------- Lists ---------------
a = [1, 2, 3, 4, 5, 6, 7]
print(a);

# includes 2nd index but not 5th 
print(a[2:5]); 

# returns whole array after 2nd index (including it)
print(a[2:]);

# returns array from 0th index to 2nd index (not including 2nd index)
print(a[:2]);

# returns max
print(max(a));

# * n -> list will be concatenated n times
print(a*3);

# ---------- Tuples ---------------
b = (1, 2, 3, 4, 5);
print(b);

# Tuple can't be updated while list can be
# b[2] = 2

c = ("abhay", "ray");
print(c+b);

# convert list to tuple
print(tuple(a));

# convert tuple to list
print(list(b));

# ---------- Dictionaries ---------------

fruit = {"banana" : "yellow", "apple" : "red"};
print(fruit);
print(fruit["apple"]);

fruit["grape"] = "green";
print(fruit);

del fruit["apple"]
print(fruit)


