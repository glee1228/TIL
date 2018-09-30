def computeLongestPalindrome(text):
    # cost_matrix = [[None] * len(text) for i in range(len(text))]  # 2-dimensional list

    # BEGIN_YOUR_CODE
    # the below code don't exploit dynamic progrmming

    def get_cost(i, j):
        if i == j:
            return 1
        elif i > j:
            return 0
        elif text[i] == text[j]:
            return get_cost(i + 1, j - 1) + 2
        else:
            return max(get_cost(i, j - 1), get_cost(i + 1, j))

    return get_cost(0, len(text) - 1)
    # END_YOUR_CODE
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
    print(next_word_set_dict)
    sentences = []
    stack = []

    def mutate_sentence_r(word):
        stack.append(word)  # push something
        if len(stack) == len(input_words):
            sentences.append(' '.join(stack))
        else:
            for next_word in next_word_set_dict[word]:
                mutate_sentence_r(next_word)
        stack.pop()

    for word in word_set:
        mutate_sentence_r(word)

    return sentences

def main():
    print(computeLongestPalindrome("animal"))
    print(mutateSentences("a b a c"))
main()