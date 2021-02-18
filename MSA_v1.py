from Bio import Phylo

MSA Tool

#Start of the Sprint_3 project

import  bio # biopython provides modules and scripts for python based bioinformaticians
import  datetime # a module that allows classes to manipulate dates and times
import  OS # a module that interacts with an operating system to create folders
import  time # a module that provides time related functions
import  xml.etree.ElementTree # A module that has an API for parsing and creating XML data
import sentry_sdk # Enables automatic reporting of errors and exceptions

From Bio Import Entrez, BioSeqIO, BioAlignIO, Phylo # Entrez provides code to access the NCBI over the www, BioSeqIO standard sequence input/output interface for biopython (only dealing in RefSeq objects), BioAlign works directly with sequence alignment files as alignment objects, phylo provides classes and functions to support phylogenetic trees
From Bio.Blast Import NCBIWWW # Modules enables www version of NCBI BLAST to be accessed
From Bio.Cluster Import Node, Tree, treecluster # Nodes describes a single node in a hierarchical clustering tree, Tree performs a hierarchical clustering tree consisting of nodes and tree cluster also creates a hierarchical clustering tree but returns a tree object


def get_query_name():
    query_name = input('Please enter name for this query: ')
    while not query_name:
        query_name = input('Please enter name for this query: ')

    current_dir = os.getcwd()
    path_name = current_dir + '/' + query_name

    sentry = False
    while sentry == False:
        if not os.path.exists(path_name):
            os.mkdir(path_name)
            sentry = True

        else:
            print('Folder already exists, please choose another name')
            query_name = input('Please enter a name for this query: ')
            path_name = current_dir + '/' + query_name

    return query_name, path_name