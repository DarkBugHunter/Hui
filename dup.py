import os

try:
    os.mkdir("Cleaned Files")
except:
    pass

try:
    os.chdir("/home/darkweb/Bug/File")
except:
    print("Wrong Path Exiting ...")
    exit()

linesSet = set()
FileCount = int(input("How Many File You Have :- "))
fileName = 1
outFile = 1
folderPath = "/home/darkweb/Bug/Cleaned Files/"

for i in range(FileCount):
    newFilein = "file" + str(fileName) + ".txt"
    newFileout = folderPath + "file" + str(outFile) + ".txt"
    outfile2 = open(newFileout, "w")
    infile = open(newFilein, "r")
    for line in infile:
        if line not in linesSet:
            outfile2.write(line)
            linesSet.add(line)
    outfile2.close()
    fileName += 1
    outFile  +=1
    
print("Done")
