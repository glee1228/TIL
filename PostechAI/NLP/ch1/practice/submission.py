# -*- coding: utf-8 -*-

import collections

_X_ = None

############################################################
# Problem A

def computeMaxWordLength1(text):
    """
    Given a string |text|, return the longest word in |text|.  If there are
    ties, choose the word that comes latest in the alphabet.
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE
    # raise NotImplementedError
    words = text.split()
    max_word = words[0]
    for word in words:
        if len(word) > len(max_word):
            max_word = word
        elif len(word) == len(max_word) and word > max_word:
            max_word = word
    return max_word
    # END_YOUR_CODE

def computeMaxWordLength2(text):
    # BEGIN_YOUR_CODE
    # raise NotImplementedError
    def my_max(values, key):
        max_value = values[0]
        for value in values:
            if key(value) > key(max_value):
                max_value = value
        return max_value

    def key(value):
        return (len(value), value)

    return my_max(text.split(), key)
    # END_YOUR_CODE

def computeMaxWordLength3(text):
    # BEGIN_YOUR_CODE
    # raise NotImplementedError
    return max(text.split(), key=lambda x: (len(x), x))
    # END_YOUR_CODE

############################################################
# Problem B

def computeMostFrequentWord(text):
    """
    Splits the string |text| by whitespace and returns two things as a pair: 
        the set of words that occur the maximum number of times, and
    their count, i.e.
    (set of words that occur the most number of times, that maximum number/count)
    You might find it useful to use collections.defaultdict(float).
    """
    # BEGIN_YOUR_CODE
    # raise NotImplementedError
    count_dict = collections.defaultdict(int)
    for word in text.split():
        count_dict[word] += 1   # increase the frequency of 'word'
    max_count = max(count_dict.values())        # use dict.values()
    most_frequent_words = set(word for word, count in count_dict.items() if count == max_count)  # choose words whose count is 'max_count'
    return most_frequent_words, max_count
    # END_YOUR_CODE

############################################################
# Problem C

def computeLongestPalindrome0(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE
    # the below code don't exploit dynamic progrmming
    # raise NotImplementedError

    def get_cost(i, j):
        if i == j:
            return 1
        elif i > j:
            return 0
        elif text[i] == text[j]:
            return get_cost(i + 1, j -1) + 2
        else:
            return max(get_cost(i, j - 1), get_cost(i + 1, j))

    return get_cost(0, len(text) - 1)
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
    # cost_matrix[i][j]
    # BEGIN_YOUR_CODE
    def get_cost(i, j):
        if i == j:
            return 1
        elif i > j:
            return 0
        else:
            if not cost_matrix[i][j]:
                if text[i] == text[j]:
                    cost_matrix[i][j] = get_cost(i + 1, j - 1) + 2
                else:
                    cost_matrix[i][j] = max(get_cost(i, j - 1), get_cost(i + 1, j))
            return cost_matrix[i][j]

    return get_cost(0, len(text) - 1)
    # END_YOUR_CODE


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


fibo_numbers = [0, 1]

def fibo_dynamic(n):
    fibo_numbers.extend([None] * max(n - len(fibo_numbers) + 1, 0))

    def fibo_r(n):
        if fibo_numbers[n] is None:
            fibo_numbers[n] = fibo_r(n-1) + fibo_r(n-2)
        return fibo_numbers[n]

    return fibo_r(n)

############################################################
# Problem D

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
    input_words = sentence.split()
    word_set = set(input_words)
    next_word_set_dict = {word: set() for word in word_set}

    for i in range(len(input_words) - 1):
        next_word_set_dict[input_words[i]].add(input_words[i + 1])

    sentences = []
    stack = []

    def mutate_sentence_r(word):
        stack.append(word)          # push something
        if len(stack) == len(input_words):
            sentences.append(' '.join(stack))
        else:
            for next_word in next_word_set_dict[word]:
                mutate_sentence_r(next_word)
        stack.pop()
    
    for word in word_set:
        mutate_sentence_r(word)

    return sentences

    # END_YOUR_CODE

############################################################
# Problem E

def manhattanDistance(loc1, loc2):
    """
    Return the Manhattan distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE
    # raise NotImplementedError
    # use 'abs'
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
    # END_YOUR_CODE

############################################################
# Problem F

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collection.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE
    if len(v2) < len(v1):
        v1, v2 = v2, v1
    return sum(v1.get(key, 0) * v2.get(key, 0) for key in v1)
    # raise NotImplementedError
    # END_YOUR_CODE

############################################################
# Problem G

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE
    # raise NotImplementedError
    for key, val in v2.items():
        v1[key] = v1[key] + scale * val
    # use dict.items
    # END_YOUR_CODE

