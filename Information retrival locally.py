from Bio import SeqIO


#convert data from genbank file to Fasta file

count = SeqIO.convert("ls_orchid.gbk", "genbank", "my_file.fasta", "fasta")


seq_record = SeqIO.parse("Covid-19.gbk", "genbank")

record=next(seq_record)

print(record.annotations['molecule_type'])
print(record.annotations['comment'])
print(record.annotations['molecule_type'])
print(record.annotations['topology'])
print(record.annotations['data_file_division'])
print(record.annotations['date'])
print(record.annotations['accessions'])
print(record.annotations['sequence_version'])
print(record.annotations['keywords'])
print(record.annotations['source'])
print(record.annotations['organism'])
print(record.annotations['taxonomy'])
print(record.annotations['references'])


# print(seq_record.annotations)