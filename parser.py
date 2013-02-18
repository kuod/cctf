import csv,re,textwrap,sys
inputFile = sys.argv
with open(inputFile[1], "rU") as csvfile:
    fastaname = csvfile.name.split(".")[0]
    filereader = csv.reader(csvfile, delimiter=',')
    rowcount = 0 
    output = open(fastaname + ".fasta", 'w')
    for row in filereader:
	if any("NC_" in s for s in row):
                header = ">" + row[0]
		rowcount = 1
		print("header initialized")
	elif(rowcount == 1):
	    if any("Start" in s for s in row):
		name = ''.join(row[0].split())
		print("name initialized")
		rowcount = 2
	else:
                """
                if(rowcount == 2):
                    rowHeader = header + "|" + row[1] + "|" + row[2] + "|" + name
                    output.write(rowHeader + '\n')
                    output.write('\n'.join(textwrap.wrap(row[0], 80)))
                    rowcount += rowcount + 1
                """
                if (len(row[0]) != 0):
                    rowHeader = header + "|" + row[1] + "|" + row[2] + "|" + name
                    output.write(rowHeader + '\n')
                    output.write('\n'.join(textwrap.wrap(row[0], 80)) + '\n')
                    rowcount += rowcount + 1
    print(rowcount.real)
    output.close()
csvfile.close()
