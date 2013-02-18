cctf
====

convert csv to fasta

A small parser that takes in a CSV file and outputs the the input into FASTA

Assumptions:
1   header begins with "NC_"
2   Start is in column 2
3   End is in column 3
4   Genome of interest is in row 2
5   Prints the full sequence limited to 80 characters
