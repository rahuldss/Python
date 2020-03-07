import os

# x = create
# r = read
# w = read/write
# a = append
newFile=open("myFile1.txt","r")

newFile.mode
newFile.name
newFile.softspace()

# for i in range(1,10):
#     newFile.write("Line No.\n")

# for i in range(1,10):
#     print(newFile.read())

newFile.seek(5)
newFile.read()

# os.rename("myFile1.txt","newFile1.txt")
# os.remove("myFile1.txt")

newFile.close()