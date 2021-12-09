#!/user/bin/python3

"""
BPSM 2021, Final Exam
Part 2 - Implementation
Student: B195515-2021
"""

Plasmodium simium

write a Python3 programme that will enable us to run BLAST analyses of
whatever we want without using a browser

enable the user to make BLAST database(s) and
then do BLAST analyses. You will need to run blast on the server from within
Python using modules

what is going to be needed,
and what are the inputs, processing, and outputs), and how you will minimize what
the user does incorrectly
Describe features/aspects of your code that will enable the user to choose what they
want to do with their data.
Include all your code features/aspects that you have thought of, even if you don’t
manage to implement all of them in Part 2: Implementation.

"""Setup environment"""
import os, sys, subprocess, re
import numpy as np
import pandas as pd
from glob import glob

def shell(cmd):
	""" Executes a shell command """
	return subprocess.call(cmd, shell = True)

def lines():
	return '-'*70

"""User inquiry"""
input_type = {'DNA','PROTEIN'}
while True:
	in_query = input('Enter query type: DNA or Protein\n\t').upper()
	in_database = input('Enter database type: DNA or Protein\n\t').upper()
	try:
		if in_query in input_type and in_database in input_type:
			in_querydatabase = in_query+in_database
			# DNAq, DNAdb
			if in_querydatabase == DNADNA:
				blasttype = blastn
			# DNAq, PROTdb
			elif in_querydatabase == DNAPROTEIN:
				blasttype = blastx
			# PROTdb, DNAq
			elif in_querydatabase == PROTEINDNA:
				blasttype = tblastn
			# PROTdb, PROTq
			elif in_querydatabase == PROTEINPROTEIN:
				blasttype = blastp

			print(f'{lines()}\nQuery type:\t{in_query}\nDatabase type:\t{in_database}\n{lines()}')
			break
		else:
			print('Incorrect input. Please try again.')
			continue
	except:
		continue


"""Create database
"""

# Retrieve sequences to construct database
wget <url>

grep -c ">" <filename>.fasta

# Show what's in the sequence file
cat <filename>.fasta | awk '{ if(substr($1,1,1)=='>')'...

# Format sequences into a db
makeblastdb -in <filename>.fasta -dbtype prot -out <dbname>

# Show the database file types
ls -l <dbname>*


"""Retrieve sequences to search FOR
"""

# On the go
wget -O <searchfile>.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=<database>&id=<accessionID>&strand=1&seq_start=<int>&seq_stop=<int>&rettype=fasta&retmode=text"


"""Cleanup"""

"""END"""