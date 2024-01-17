n = int(input("Enter the number of elements in list: "))
l = []
for _ in range(n):
    l.append(int(input()))

print(f"List is {l}")
# Inbuilt method
meth1 = l[:]
meth1.reverse()
print(f"Reversed list from Method 1: {meth1}")
# String Slicing
meth2 = l[::-1]
print(f"Reversed list from Method 2: {meth2}")
# Swapping
meth3 = l[:]
for i in range(int(n/2)):
    meth3[i], meth3[n-i-1] = meth3[n-i-1], meth3[i]
print(f"Reversed list from Method 3: {meth3}")
if meth1 == meth2 == meth3:
    print("All methods returns the same result")
