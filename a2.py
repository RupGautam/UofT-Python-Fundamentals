def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

def is_valid_sequence(dna):
	"""
	(str) -> bool

	Return True if and only DNA sequence is valid (which contains nucleotides: 'A', 'T', C', 'G').

	>>> is_valid_sequence('ATCGQATCG')
	True
	>>> is_valid_sequence('aAT')
	False
	"""

	# valid_dna_sequence = 'ATCG'

	# for nucleotides in dna:
	# 	if nucleotides not in valid_dna_sequence:
	# 		return False
	# return True

	result = True
	valid_dna_sequence = 'ATCG'
	for nucleotides in dna:
		if nucleotides not in valid_dna_sequence:
			result = False
	return True




















