from Bio import SeqIO


def overlap_graphs(path: str, k: int):
    with open(path) as f:
        fasta_sequences = list(SeqIO.parse(f, "fasta"))
    for i in fasta_sequences:
        for j in fasta_sequences:
            name1, sequence1 = i.id, str(i.seq)
            name2, sequence2 = j.id, str(j.seq)
            if sequence1 == sequence2:
                continue
            suffix = sequence1[-k:]
            prefix = sequence2[:k]
            if prefix == suffix:
                print(name1, name2)
