import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, item):
        if self.value == item:
            return False
        elif item < self.value:
            if self.left:
                return self.left.insert(item)
            else:
                self.left = Node(item)
                return True
        else:
            if self.right:
                return self.right.insert(item)
            else:
                self.right = Node(item)
                return True


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, item):
        if self.root:
            return self.root.insert(item)
        else:
            self.root = Node(item)
            return True

tree = BST()

for name in names_1:
    if tree.insert(name):
        pass
    else:
        if name not in duplicates:
            duplicates.append(name)

for name in names_2:
    if tree.insert(name):
        pass
    else:
        if name not in duplicates:
            duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# This is the fastest way I could find to do it however it does not find duplicates within the contained files and only
# the duplicates across the 2 files.
for name in set(names_1).intersection(names_2):
    duplicates.append(name)
