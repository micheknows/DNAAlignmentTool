from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def align_sequences(seq1, seq2):
    """
    Align two DNA sequences using Biopython's pairwise2 module.
    """
    # Perform global alignment
    alignments = pairwise2.align.globalxx(seq1, seq2)

    # Return the first alignment (for simplicity)
    # You might want to handle multiple alignments differently
    return format_alignment(*alignments[0])

# Example usage:
if __name__ == "__main__":
    seq1 = "GATTACA"
    seq2 = "GCATGCU"

    alignment = align_sequences(seq1, seq2)
    print(alignment)
