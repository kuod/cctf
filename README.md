cctf
====

convert csv to fasta

A small parser that takes in a CSV file and outputs the the input into FASTA. Included is an Excel macro that outputs each sheet as a CSV file. The python script parser.py requires csv, re, textwrap and sys modules. The first cell is believed to contain the name of the genome and the remainder of the header is comprised of the start, end and additional metadata such as the csv filename.
