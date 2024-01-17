N = int(input())
string = list(input())
addNum = int(input())

length = len(string)
for i in range(length):
	if ord("Z") >= ord(string[i]) >= ord("A"):
		asciiCode = ord(string[i]) + addNum
		while asciiCode > ord("Z"):
			asciiCode = asciiCode - ord("Z") + ord("A") - 1
		string[i] = chr(asciiCode)
	elif ord("z") >= ord(string[i]) >= ord("a"):
		asciiCode = ord(string[i]) + addNum
		while asciiCode > ord("z"):
			asciiCode = asciiCode - ord("z") + ord("a") - 1
		string[i] = chr(asciiCode)

print("".join(string))
