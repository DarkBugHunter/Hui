import os
import glob

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
txtFiles = []

for files in glob.glob("*.txt"):
    txtFiles.append(files)

print(f"Found {len(txtFiles)} txt Files")

fileName = 1
outFile = 1
folderPath = "/home/darkweb/Bug/Cleaned Files/"

for i in range(len(txtFiles)):
    newFileout = folderPath + txtFiles[i]
    outfile2 = open(newFileout, "w")
    infile = open(txtFiles[i], "r")
    for line in infile:
        if line not in linesSet:
            outfile2.write(line)
            linesSet.add(line)
    outfile2.close()
    
print("Done")
