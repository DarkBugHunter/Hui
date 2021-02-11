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

if len(txtFiles) == 0:
    print("Oops No txt Files Found")
    exit()
    
print(f"Found {len(txtFiles)} txt Files")


folderPath = "/home/darkweb/Bug/Cleaned Files/"

for i in range(len(txtFiles)):
    newFileout = folderPath + txtFiles[i]
    outfile2 = open(newFileout, "w")
    infile = open(txtFiles[i], "r")
    for line in infile:
        if line.lower() not in linesSet:
            outfile2.write(line)
            linesSet.add(line.lower())
    outfile2.close()
    
print("Done")
