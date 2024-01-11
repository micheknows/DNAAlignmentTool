from flask import Blueprint, render_template, request, flash, redirect, url_for
from .alignment import align_sequences
import Bio.Align as align
from Bio.Align import PairwiseAligner

# Create a Blueprint for the DNA tool
dna_tool_bp = Blueprint('dna_tool', __name__)

@dna_tool_bp.route('/')
def dna_index():
    # Render the index page specific to the DNA Alignment Tool
    return render_template('dna_index.html')


def count_gaps(aligned):
    """Count gap characters in aligned sequence"""

    gaps = 0

    for base in aligned:
        if base == "-":
            gaps += 1

    return gaps


def count_identities(aligned, seq1, seq2):
    # Determine max length
    max_len = max(len(seq1), len(seq2), len(aligned))

    # Pad sequences so same length
    seq1 += "-" * (max_len - len(seq1))
    seq2 += "-" * (max_len - len(seq2))

    identities = 0

    for i in range(len(aligned)):
        if seq1[i] == aligned[i] and seq2[i] == aligned[i]:
            identities += 1

    return identities

def get_alignment_stats(seq1, seq2, aligned):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    len_aligned = len(aligned)

    aligner = PairwiseAligner()  # BioPython aligner
    matrix = aligner.substitution_matrix  # actual matrix

    gap_open = aligner.gap_score
    gap_extend = aligner.extend_gap_score

    identity = count_identities(aligned, seq1, seq2)
    percent_id = 100 * identity / len_aligned

    gaps = count_gaps(aligned)
    percent_gaps = 100 * gaps / len_aligned



    # Calculate score
    score = aligner.score(seq1, seq2)

    return {
        'type': 'DNA',
        'matrix': matrix,
        'gap_penalty': gap_open,
        'extend_penalty': gap_extend,
        'score': score,
        'len_seq1': len_seq1,
        'len_seq2': len_seq2,
        'len_aligned': len_aligned,
        'identities': f'{identity}/{len_aligned} ({percent_id:.2f}%)',
        'gaps': f'{gaps}/{len_aligned} ({percent_gaps:.2f}%)',
    }

def build_alignment_string(alignment):
    """ Returns HTML string showing alignment matches/mismatches """
    # Initialize HTML string for each line
    seq1_html = ""
    seq2_html = ""
    alignment_html = ""
    alignmentChar = alignment.strip().split('\n')[1]
    seq1 = alignment.strip().split('\n')[0]
    seq2 = alignment.strip().split('\n')[2]

    # Iterate over both sequences and alignment, add styled spans to the HTML string
    for base1, base2, align_char in zip(seq1, seq2, alignmentChar):
        seq1_class = "match" if base1 == base2 else "mismatch"
        seq2_class = "match" if base1 == base2 else "mismatch"

        seq1_html += f"<span class='{seq1_class}'>{base1}</span>"
        alignment_html += f"<span class='align'>{align_char}</span>"
        seq2_html += f"<span class='{seq2_class}'>{base2}</span>"

    # Combine the lines into a single HTML string
    combined_html = f"<div>{seq1_html}</div><div>{alignment_html}</div><div>{seq2_html}</div>"

    return combined_html


@dna_tool_bp.route('/align', methods=['GET', 'POST'])
def align():
    if request.method == 'POST':
        seq1 = request.form.get('seq1')
        seq2 = request.form.get('seq2')

        # Basic validation to check if sequences are entered
        if not seq1 or not seq2:
            flash('Please enter both sequences.')
            return redirect(url_for('dna_tool.align'))
    if request.method == 'POST':

        # Perform alignment
        alignment_result = align_sequences(seq1, seq2)
        alignment_html = build_alignment_string(alignment_result)


        alignment_stats = get_alignment_stats(seq1, seq2, alignment_result)

        # Pass the alignment HTML to the template
        return render_template('results.html',
                               alignment=alignment_result,
                               alignment_html = alignment_html,
                               stats=alignment_stats)

    # Render the alignment input form page
    return render_template('align.html')
