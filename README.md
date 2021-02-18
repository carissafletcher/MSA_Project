# MSA Project

Sprint_3 Team Coding Project

MSA is a tool that creates Multiple Sequence Alignments and analyses for mRNA protein coding sequences across different species.

To use this tool the input must be a Refseq NCBI database accession number with the prefix NM_

The NM_ prefix corresponds to a mRNA protein coding transcript. 

The tool will perform the following funtions

1. Parse a GENBANK database record using a NM_accession number using BIOPYTHON
2. Extract the mRNA sequence for the NM_ record from GENBANK
3. Extract the protein associated (NP_) with the NM_ accession number
4. Extract the protein sequence associated with the retrieved NP_accession number 
5. Create a blast search for the mRNA and protein sequences across several organisms
6. Create a clustal alignment for the mRNA and protein sequences across several organisms
7. The files generated from this tool will be deposited in a new directory, based on the users initial input