import Bio
from Bio import Entrez
from Bio.Seq import Seq
from Bio.Seq import *
from Bio.Alphabet import *
Entrez.email = 'Abdo45010@gmail.com'

ID=input("Enter your Accession number please : " )
print("\r") 
handle = Entrez.efetch(db="nucleotide", id=ID, retmode="xml")
record = Entrez.read(handle)
handle.close()
print("Organism            :  ",record[0]["GBSeq_source"])
print("\r") 
print("Sequence Length     :  ",record[0]["GBSeq_length"])
print("\r") 
print("Sequence Standedness:  ",record[0]["GBSeq_strandedness"])
print("\r") 
print("Version             :  ",record[0]["GBSeq_accession-version"])
print("\r") 
print("Taxonomy            :  ",record[0]["GBSeq_taxonomy"])
print("\r") 
print("Sequence Definition : ",record[0]["GBSeq_definition"])
print("\r") 
print("Keyword             : ",record[0]["GBSeq_keywords"])
print("\r") 
print("Create Date         : ",record[0]["GBSeq_create-date"])
print("\r") 
print("Update Date         : ",record[0]["GBSeq_update-date"])
print("\r") 
print("The Sequence:       : ",record[0]["GBSeq_sequence"])
print("\r") 
		  
seq=Seq(record[0]["GBSeq_sequence"])
SEQ=Seq(seq, IUPAC.unambiguous_dna)
