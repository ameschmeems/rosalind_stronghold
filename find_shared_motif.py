from Bio import SeqIO

def shared_motif(path: str):
    with open(path) as f:
        sequences = list(SeqIO.parse(f, 'fasta'))
    min_len = len(str(sequences[0].seq))
    min_index = 0
    for i in range(len(sequences)):
        if len(str(sequences[i].seq)) < min_len:
            min_len = len(str(sequences[0].seq))
            min_index = i
    motif = ''
    for i in range(len(str(sequences[min_index].seq))):
        n = 0
        present = True
        while present:
            for j in sequences:
                if str(sequences[min_index].seq)[i:i+n] not in str(j.seq) or n > 1000:
                    present = False
                    break
            if present:
                motif = max(str(sequences[min_index].seq)[i:i+n], motif, key=len)
            n += 1
    return motif
