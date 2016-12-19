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


def  insert_sequence(seq_1, seq_2, index):
	"""
	(str, str, int) -> str

	Return dna sequence index accordingly by inserting and index DNA sequence.
	The first and second parameters are valid(assuming, it's a valid input) DNA sequences and the third parameter is index position.

	>>> insert_sequence('CCGG', 'AT', 2)
	'CCATGG'
	insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'
	"""
	return seq_1[:index] + seq_2 + seq_1[index:]


def get_complement(nucleotides):
	"""
	(str) -> str

	Return the given nucleotides's complement.
	The first parameter is nucleotides: 'A','T','C','G'

	Side note: A complements T and visa-versa
					A - T
					T - A
			   C complements G and visa-versa
					C - G
					G - C
	>>> get_complement('A')
	'T'
	>>> get_complement('C')
	'G'
	>>> get_complement('T')
	'A'
	>>> get_complement('G')
	'C'
	"""

	if nucleotides == 'A':
		return 'T'
	elif nucleotides == 'T':
		return 'A'
	elif nucleotides == 'C':
		return 'G'
	elif nucleotides == 'G':
		return 'C'
	else:
		print("Please enter valid nucleotides 'ACTG'")


















