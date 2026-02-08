# Importing array module
import array as arr

# -------------------------------------------------
# Creating an array
# 'i' means array of signed integers
# -------------------------------------------------
a = arr.array('i', [10, 20, 30, 40, 50])
print("Original array:", a)

# -------------------------------------------------
# Accessing elements (indexing)
# -------------------------------------------------
print("First element:", a[0])
print("Last element:", a[-1])

# -------------------------------------------------
# Traversing array using loop
# -------------------------------------------------
print("Traversing array:")
for i in a:
    print(i)

# -------------------------------------------------
# Length of array
# -------------------------------------------------
print("Length of array:", len(a))

# -------------------------------------------------
# Append element (add at end)
# -------------------------------------------------
a.append(60)
print("After append:", a)

# -------------------------------------------------
# Insert element at specific index
# insert(index, value)
# -------------------------------------------------
a.insert(2, 25)
print("After insert:", a)

# -------------------------------------------------
# Extend array (add multiple elements)
# -------------------------------------------------
a.extend([70, 80, 90])
print("After extend:", a)

# -------------------------------------------------
# Remove element by value (first occurrence)
# -------------------------------------------------
a.remove(25)
print("After remove:", a)

# -------------------------------------------------
# Pop element (remove by index, default last)
# -------------------------------------------------
popped = a.pop()
print("Popped element:", popped)
print("After pop:", a)

# -------------------------------------------------
# Index of an element
# -------------------------------------------------
print("Index of 40:", a.index(40))

# -------------------------------------------------
# Count occurrences of an element
# -------------------------------------------------
print("Count of 20:", a.count(20))

# -------------------------------------------------
# Reverse the array
# -------------------------------------------------
a.reverse()
print("After reverse:", a)

# -------------------------------------------------
# Convert array to list
# -------------------------------------------------
list_version = a.tolist()
print("Array to list:", list_version)

# -------------------------------------------------
# Slice array
# -------------------------------------------------
print("Sliced array (index 1 to 4):", a[1:4])

# -------------------------------------------------
# Update element at index
# -------------------------------------------------
a[0] = 100
print("After updating index 0:", a)

# -------------------------------------------------
# Delete element using del
# -------------------------------------------------
del a[1]
print("After deleting index 1:", a)

# -------------------------------------------------
# Concatenation of arrays
# -------------------------------------------------
b = arr.array('i', [1, 2, 3])
c = a + b
print("After concatenation:", c)

# -------------------------------------------------
# Membership test
# -------------------------------------------------
print("Is 40 in array?", 40 in a)

