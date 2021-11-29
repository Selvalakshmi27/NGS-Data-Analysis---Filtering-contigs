#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Bio
from Bio import SeqIO
from Bio.SeqIO.FastaIO import SimpleFastaParser


# In[2]:


#To filter contigs by length
def contigs_by_length(input_file,size,output_file):    # Specify input fasta, size to be filtered, output fasta file
    contigs = []                                       # Empty list
    for records in SeqIO.parse(input_file,"fasta"):    # Parse through records in the input file
        if len(records) >= size:                       # Mention the minimum size of contigs to keep
            contigs.append(records)                    # Keep only the records that are above the mentioned size
            SeqIO.write(contigs,output_file,"fasta")   # Write the results to the output file


# In[3]:


#To filter contigs by coverage
def contig_by_coverage(input_file,cov):                # Specify input fasta file, minimum coverage
    with open (input_file) as in_handle:               # opening the input file          
        for title,seq in SimpleFastaParser(in_handle): # Parsing through the file with SimpleFastaParser (High throughput)             
            split = title.split("_")                   # Removing "_" from the headers/title of each contig
            coverage = split[5]                        # Selecting the 5th column of the title (coverage column)
            if float(coverage) >=cov:                  # Keep only titles above the minimum coverage
                coverage = []
                coverage.append(title)
                print(title)                           # Results
                print(seq)


# In[23]:


#To filter contigs by both length and coverage
#To replace the headers with blank space
def filter_contigs(input_file,size,cov):                      # File to be filtered,required contig size, required coverage
    with open (input_file) as in_handle:                         
         for title,seq in SimpleFastaParser(in_handle):       # Parsing through the file with SimpleFastaParse           
            split = title.split("_")                          # Removing "_" from the headers/title of each contig        
            coverage = split[5]                               # Selecting the 5th column of the title (coverage column)        
            length = len(seq)                                 # To find the length of the contigs         
            if (float(coverage) >= size and length >= cov):   # Keep the contigs above the minimum size and coverage
                coverage = []                                 # Creating empty list
                length = []
                length.append(seq) and coverage.append(title) 
            
            out = title.replace(title," ")                    #To replace the headers with blank space
            print(out)
            print(seq)
            
            
                  


# In[ ]:




