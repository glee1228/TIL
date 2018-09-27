import collections

def computeMaxWordLength1(text):
    """
    Given a string |text|, return the longest word in |text|.  If there are
    ties, choose the word that comes latest in the alphabet.
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE
    words = text.split()
    max_word = words[0]
    for word in words:
        if len(word)>len(max_word):
            max_word = word
        elif word > max_word and len(word)==len(max_word):
            max_word = word
    return max_word
    # END_YOUR_CODE

def computeMaxWordLength2(text):
    # BEGIN_YOUR_CODE

    def my_max(values, key):
        max_value = values[0]
        for value in values:
            if key(value) > key(max_value):
                max_value = value
        return max_value

    def key(value):
        return (len(value),value)

    return my_max(text.split(), key)
    # END_YOUR_CODE

def computeMaxWordLength3(text):
    # BEGIN_YOUR_CODE
    return max(text.split(), key=lambda x: (len(x),x))

def computeMostFrequentWord(text):
    """
    Splits the string |text| by whitespace and returns two things as a pair:
        the set of words that occur the maximum number of times, and
    their count, i.e.
    (set of words that occur the most number of times, that maximum number/count)
    You might find it useful to use collections.defaultdict(float).
    """
    # BEGIN_YOUR_CODE
    count_dict = collections.defaultdict(int)
    for word in text.split():
        count_dict[word]+=1  # increase the frequency of 'word'
    max_count = max(count_dict.values())  # use dict.values()
    most_frequent_words = set(
        word for word, count in count_dict.items() if count==max_count)  # choose words whose count is 'max_count'
    return most_frequent_words, max_count
    # END_YOUR_CODE
def manhattanDistance(loc1, loc2):
    """
    Return the Manhattan distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE
    return abs(loc1[0]-loc2[0])+abs(loc1[1]-loc2[1])
    # use 'abs'
    # END_YOUR_CODE

def computeLongestPalindrome(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    cost_matrix = [[None] * len(text) for i in range(len(text))]  # 2-dimensional list

    # BEGIN_YOUR_CODE

    # END_YOUR_CODE


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


fibo_numbers = [0, 1]


def fibo_dynamic(n):
    fibo_numbers.extend([None] * max(n - len(fibo_numbers) + 1, 0))

    def fibo_r(n):
        if fibo_numbers[n] is None:
            fibo_numbers[n] = fibo_r(n - 1) + fibo_r(n - 2)
        return fibo_numbers[n]

    return fibo_r(n)

def mutateSentences(sentence):
    """
    High-level idea: generate sentences similar to a given sentence.
    Given a sentence (sequence of words), return a list of all possible
    alternative sentences of the same length, where each pair of adjacent words
    also occurs in the original sentence. (The words within each pair should appear
    in the same order in the output sentence as they did in the orignal sentence.)
    Notes:
    - The order of the sentences you output doesn't matter.
    - You must not output duplicates.
    - Your generated sentence can use a word in the original sentence more than
      once.
    """
    # BEGIN_YOUR_CODE
    
    # END_YOUR_CODE
def main():
    #print(computeMaxWordLength1("cat dog manipulation"))
    print(computeMostFrequentWord("cat dog manipulation cat"))
    print(manhattanDistance((5,5),(1,10)))
main()
