InputFile = open("input.txt", "r")
a = InputFile.readline(100)
InputFile.close()
xored = []
for i in range(len(a)):
    xored_value = ord(a[i%len(a)]) ^ 10
    xored.append(str(xored_value)[1:])
b = ''.join(xored)
OutputFILE = open("output.txt", "w")
OutputFILE.write(b)
OutputFILE.close()
