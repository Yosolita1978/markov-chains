from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_data = open(file_path)

    corpus = file_data.read()

    corpus_clean = " ".join(corpus.split())

    return corpus_clean

#    return "This should be a variable that contains your file text as one long string"


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    word_list = text_string.split()


    for i in range(len(word_list) - 3):
        key_link = (word_list[i], word_list[i+1],  word_list[i+2])
        value_list = chains.get(key_link, [])
        value_list.append(word_list[i+3])
        chains[key_link] = value_list 
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    start_key = choice(chains.keys())
    while not start_key[0][0].isupper():
        start_key = choice(chains.keys())

    runing_key = start_key
    while True:
        text += runing_key[0] + ' ' + runing_key[1] + ' ' + runing_key[2]
        try:
            text_value = choice(chains[runing_key])
            if text_value.endswith("?", -2, -1):
                break
        except KeyError:
            break
        text = text + ' ' + text_value + ' '
        runing_key = (runing_key[1], runing_key[2], text_value)  

    return text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

#print chains

# Produce random text
random_text = make_text(chains)

print random_text
