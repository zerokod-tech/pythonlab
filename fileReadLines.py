import os
file = open("/Users/roberta/Documents/IOSDEV/PythonLab/PythonTest/testo.txt","r")
#print(file.read())
print(file.readlines())
#file.write("Sunday")
##file.write("Monday")
#file = open("/Users/roberta/Documents/IOSDEV/PythonLab/PythonTest.writetest.txt","x")
"""if os.path.exists("/Users/roberta/Documents/IOSDEV/PythonLab/PythonTest/file.txt"):
        os.remove("writetest.txt")
else:
    print(" There is no file")

for line in file:
      print(file.readlines())"""

file.close()