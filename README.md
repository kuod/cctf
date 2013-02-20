cctf
====

convert csv to fasta

A small parser that takes in a CSV file and outputs the the input into FASTA

Assumptions:\n
1   header is the first cell \n
2   Start is in column 2 \n
3   End is in column 3 \n
4   Genome of interest is in row 2 \n
5   Prints the full sequence limited to 80 characters \n
