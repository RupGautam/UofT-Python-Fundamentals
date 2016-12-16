def collect_vowels(s):
    ''' (str) -> str

    Return vowels from s. do not treat y as vowel.
    >>> collect_vowels('Happy Birthday')
    'aia'
    >>> collect_vowels('xyz')
    ''
    '''
    vowels = ''
    num_vowels = 0

    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    print ("There are", num_vowels, "vowel letters in", s, "and those are -->", vowels)



##def count_vowels(s):
##    '''(str) -> int
##
##    Return the number of vowels in s. Do not treat y as a vowel.
##
##    >>> count_vowels('Happy Birthday')
##    3 
##    >>> count_vowels('xyz')
##    0 s
##    '''
##
##    num_vowels = 0
##    for char in s:
##        if char in 'aeiouAEIOU':
##            num_vowels = num_vowels + 1 
##
##    return num_vowels

