# Opening/Closing a file

# f = open('sample', 'r')
# data = f.read()
# print(data)
# f.close()

# f = open('sample', 'a')
# f.write("Soon")
# f.close()
# f = open('sample')
# updt = f.readline()
# print(updt)
# f.close()

# Opens and Closes the file automatically

with open('sample', 'r') as f:
    a = f.read()
with open('sample', 'w') as f:
    a = f.write("Ishan")
print(a)
