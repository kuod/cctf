import csv,re,textwrap
with open('test.csv', "rU") as csvfile:
    fastaname = csvfile.name.split(".")[0]
    fastaoutput = open(fastaname + ".fasta", 'w')
    filereader = csv.reader(csvfile, delimiter=',')
    for row in filereader:
        if any("NC_" in s for s in row):
                header = ">" + row[0]
                rowcount = 1
        elif(rowcount ==1):
            if any("Length" in s for s in row):
                name = row[0].strip()
        elif(rowcount == 2):
            rowHeader = header + "|" + row[1] + "|" + row[2] + "|" + name
            outputstring += rowHeader
            outputstring += "\n".join(textwrap.wrap(row[0], 80))
     fastaoutput.write(outputstring)
    fastaoutput.close()
csvfile.close()
