
def reverse_list(l):
    """
    Reverses order of elements in list l.
    """
    ll=[]
    for i in range(len(l)-1,-1,-1):
        ll.append(l[i])
    return ll


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


# ------------------------------------------------------------------------------

def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    ss=''.join(reversed(s))
    return ss


def test_reverse_string():
    assert reverse_string("foobar") == "raboof"


# ------------------------------------------------------------------------------

def is_english_vowel(c):
    """
    Returns True if c is an english vowel
    and False otherwise.
    """
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U' or c=='Y' or c=='y':
        return True
    else:
        return False


def test_is_english_vowel():
    assert is_english_vowel('a')
    assert is_english_vowel('e')
    assert is_english_vowel('i')
    assert is_english_vowel('o')
    assert is_english_vowel('u')
    assert is_english_vowel('y')
    assert is_english_vowel('A')
    assert is_english_vowel('E')
    assert is_english_vowel('I')
    assert is_english_vowel('O')
    assert is_english_vowel('U')
    assert is_english_vowel('Y')
    assert not is_english_vowel('k')
    assert not is_english_vowel('z')
    assert not is_english_vowel('?')


# ------------------------------------------------------------------------------

def count_num_vowels(s):
    """
    Returns the number of vowels in a string s.
    """
    count=0
    for i in range(len(s)):
        if is_english_vowel(s[i]):
            count=count+1 
    return count


def test_count_num_vowels():
    sentence = "hey ho let's go"
    assert count_num_vowels(sentence) == 5
    sentence = "HEY ho let's GO"
    assert count_num_vowels(sentence) == 5
    paragraph = """She told me her name was Billie Jean,
                   as she caused a scene
                   Then every head turned with eyes
                   that dreamed of being the one
                   Who will dance on the floor in the round"""
    assert count_num_vowels(paragraph) == 54


# ------------------------------------------------------------------------------

def histogram(l):
    """
    Converts a list of integers into a simple string histogram.
    """

    li=[]
    for i in range(len(l)):
        for j in range(l[i]):
            li.append('#')
        li.append('\n')

    str=''.join(li[:len(li)-1])

    return str

def test_histogram():
    assert histogram([2, 5, 1]) == '##\n#####\n#'


# ------------------------------------------------------------------------------

def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    li=[]
    str=s.split(' ')
    for i in range(len(str)):
        li.append(len(str[i]))
    return li


def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


# ------------------------------------------------------------------------------

def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    arr=get_word_lengths(s)
    max=0
    for i in range(len(arr)):
        if arr[max] < arr[i]:
            max=i
    str=s.split(' ')
    return str[max]


def test_find_longest_word():
    text = "Three tomatoes are walking down the street"
    assert find_longest_word(text) == "tomatoes"
    text = "foo foo1 foo2 foo3"
    assert find_longest_word(text) == "foo1"


# ------------------------------------------------------------------------------

def validate_dna(s):
    """
    Return True if the DNA string only contains characters
    a, c, t, or g (lower or uppercase). False otherwise.
    """
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'c' or s[i] == 'g' or s[i] == 't' or s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            return True
        else:
            return False


def test_validate_dna():
    assert validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag')
    assert not validate_dna('xCCGGAAGAGCTTACTTAGccggaagagcttacttag')


# ------------------------------------------------------------------------------

def base_pair(c):
    """
    Return the corresponding character (lowercase)
    of the base pair. If the base is not recognized,
    return 'unknown'.
    """
    if not validate_dna(c):
        c='unknown'
    else:
        if c.lower() == 'a':
            c='t'
        elif c.lower() == 'c':
            c='g'
        elif c.lower() == 'g':
            c='c'
        elif c.lower() == 't':
            c='a'
    return c

def test_base_pair():
    assert base_pair('a') == 't'
    assert base_pair('t') == 'a'
    assert base_pair('c') == 'g'
    assert base_pair('g') == 'c'
    assert base_pair('A') == 't'
    assert base_pair('T') == 'a'
    assert base_pair('C') == 'g'
    assert base_pair('G') == 'c'
    assert base_pair('x') == 'unknown'
    assert base_pair('foo') == 'unknown'


# ------------------------------------------------------------------------------

def transcribe_dna_to_rna(s):
    """
    Return string s with each letter T replaced by U.
    Result is always uppercase.
    """
    s=s.replace('T','U')
    s=s.replace('t','U')
    return s.upper()


def test_transcribe_dna_to_rna():
    dna = 'CCGGAAGAGCTTACTTAGccggaagagcttacttag'
    assert transcribe_dna_to_rna(dna) == 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG'


# ------------------------------------------------------------------------------

def get_complement(s):
    """
    Return the DNA complement in uppercase
    (A -> T, T-> A, C -> G, G-> C).
    """
    sx=[]
    for i in range(len(s)):
        sx.append(base_pair(s[i]).upper())

    print(sx)
    c=''.join(sx)
    return c

def test_get_complement():
    assert get_complement('CCGGAAGAGCTTACTTAG') == 'GGCCTTCTCGAATGAATC'
    assert get_complement('ccggaagagcttacttag') == 'GGCCTTCTCGAATGAATC'


# ------------------------------------------------------------------------------

def get_reverse_complement(s):
    """
    Return the reverse complement of string s
    (complement reversed in order).
    """
    return ''.join(reversed(get_complement(s)[:]))


def test_get_reverse_complement():
    assert get_reverse_complement('CCGGAAGAGCTTACTTAG') == 'CTAAGTAAGCTCTTCCGG'
    assert get_reverse_complement('ccggaagagcttacttag') == 'CTAAGTAAGCTCTTCCGG'


# ------------------------------------------------------------------------------

def remove_substring(substring, string):
    """
    Returns string with all occurrences of substring removed.
    """
    string=string.replace(substring,"")
    return string

def test_remove_substring():
    assert remove_substring('GAA', 'CCGGAAGAGCTTACTTAG') == 'CCGGAGCTTACTTAG'
    assert remove_substring('CCG', 'CCGGAAGAGCTTACTTAG') == 'GAAGAGCTTACTTAG'
    assert remove_substring('TAG', 'CCGGAAGAGCTTACTTAG') == 'CCGGAAGAGCTTACT'
    assert remove_substring('GAA', 'GAAGAAGAA') == ''


# ------------------------------------------------------------------------------

def get_position_indices(triplet, dna):
    """
    Returns list of position indices for a specific triplet (3-mer)
    in a DNA sequence. We start counting from 0
    and jump by 3 characters from one position to the next.
    """
    n=3
    rli=[]
    li=[dna[i:i+n] for i in range(0,len(dna),n)]
    for j in range(len(li)):
        if li[j] == triplet:
            rli.append(j)
    return rli

def test_get_position_indices():
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAG') == [1]
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAGGAAGAA') == [1, 6, 7]


# ------------------------------------------------------------------------------
 
def get_position_indices1(triplet, dna, n):
    """
    Returns list of position indices for a specific triplet (3-mer)
    in a DNA sequence. We start counting from 0
    and jump by 3 characters from one position to the next.
    """
    sizeOfTriplet=len(triplet)
    rli=[]
    li=[dna[i:i+sizeOfTriplet] for i in range(0,len(dna),n)]
    for j in range(len(li)):
        if li[j] == triplet:
            rli.append(j)
    return rli

def get_3mer_usage_chart(s):
    """
    This routine implements a 'sliding window'
    and extracts all possible consecutive 3-mers.
    It counts how often they appear and returns
    a list of tuples with (name, occurrence).
    The list is alphabetically sorted by the name
    of the 3-mer.
    """
    n=3
    li=[]
    for i in range(len(s)-2):
        kmer=s[i:i+n]
        flagFound=False
        indices=get_position_indices1(kmer,s,1)
        if li == []:
            li.append((kmer, len(indices)))
        else:
            for j in range(len(li)):
                if kmer == li[j][0]:
                    flagFound=True
            if not flagFound:
                li.append((kmer, len(indices)))
    l=sorted(li, key=lambda tup: tup[0])
    return(l)



def test_get_3mer_usage_chart():
    s = 'CCGGAAGAGCTTACTTAGGAAGAA'
    result = []
    result.append(('AAG', 2))
    result.append(('ACT', 1))
    result.append(('AGA', 2))
    result.append(('AGC', 1))
    result.append(('AGG', 1))
    result.append(('CCG', 1))
    result.append(('CGG', 1))
    result.append(('CTT', 2))
    result.append(('GAA', 3))
    result.append(('GAG', 1))
    result.append(('GCT', 1))
    result.append(('GGA', 2))
    result.append(('TAC', 1))
    result.append(('TAG', 1))
    result.append(('TTA', 2))
    assert get_3mer_usage_chart(s) == result


# ------------------------------------------------------------------------------

def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    with open(file_name) as f:
        content = f.readlines()
    target=[]
    for i in range(len(content)):
        li=content[i]
        li=li.replace("['","")
        li=li.replace("]","")
        li=li.replace("\n", "")
        li=li.split('  ')
        if len(li) > 1:
            target.append(round(float(li[column_number-1]),3))
    return target


def test_read_column():

    import tempfile
    import os

    text = """
1   0.1  0.001
2   0.2  0.002
3   0.3  0.003
4   0.4  0.004
5   0.5  0.005
6   0.6  0.006"""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will read the column
    assert read_column(file_name, 2) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------

def character_statistics(file_name):
    """
    Reads text from file file_name, then
    lowercases the text, and then returns
    a tuple (x, y), where x is the most abundant
    and y is the least abundant character found.
    Use the isalpha() method to figure out
    whether the character is in the alphabet.
    """
    with open(file_name) as f:
        content = f.readlines()
    regis={}
    for i in range(len(content)):
        line=content[i].replace("\n", "")
        line=line.lower()
        for j in range(len(line)):
            ch=line[j]
            if ch.isalpha():
                if ch not in regis:
                    regis[ch]=1
                else:
                    regis[ch]=regis[ch]+1
    regis=sorted(regis.items(), key=lambda x: x[1])
    return (regis[-1][0],regis[0][0])


def test_character_statistics():

    import tempfile
    import os

    text = """
To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscover'd country from whose bourn
No traveller returns, puzzles the will
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all;
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry,
And lose the name of action.--Soft you now!
The fair Ophelia! Nymph, in thy orisons
Be all my sins remember'd."""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will get the stats
    (most_abundant, least_abundant) = character_statistics(file_name)
    assert (most_abundant == 'e') 
    assert (least_abundant == 'q' or least_abundant == 'z')

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------

def pythagorean_triples(n):
    """
    Returns list of all unique pythagorean triples
    (a, b, c) where a < b < c <= n.
    """
    l = []
    # loop over all a < b < c <= n
    for c in range(1, n + 1):
        for b in range(1, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    l.append((a, b, c))
    return l


# ------------------------------------------------------------------------------

def test_pythagorean_triples():
    assert pythagorean_triples(10) == [(3, 4, 5), (6, 8, 10)]
    assert pythagorean_triples(20) == [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)]
    assert pythagorean_triples(30) == [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20), (15, 20, 25), (7, 24, 25), (10, 24, 26), (20, 21, 29), (18, 24, 30)]

