linesSet = set()
fileName = input("Enter File Name (include extension too file email.txt :- ")
outFile = input("With What Name You want to save the file (include extension too :- ")
outfile2 = open(outFile, "w")
infile = open(fileName, "r")
for line in infile:
    if line not in linesSet:
        outfile2.write(line)
        linesSet.add(line)
outfile2.close()
print("")
print("File Successfully Saved as ", outFile)
