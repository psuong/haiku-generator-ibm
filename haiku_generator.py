from sample_database import words
from random import randint

def generate_line(syllable_count):
    # TODO: Generate the logic which defines the line in a haiku
    pass

def generate_random_lines():
    # TODO: Generate the line by randomly selecting words, this should be relatively
    # easy to do
    haiku = []
    word_one = words[1][randint(0, len(words[1])-1)]
    word_two = words[2][randint(0, len(words[2])-1)]
    word_three = words[3][randint(0, len(words[3])-1)]
    word_four = words[4][randint(0, len(words[4])-1)]
    word_five = words[5][randint(0, len(words[5])-1)]
    word_six = words[6][randint(0, len(words[6])-1)]
    word_seven = words[7][randint(0, len(words[7])-1)]

    haiku.append("%s %s" % (word_one, word_two))
    haiku.append("%s %s %s," % (word_three, word_four, word_five))
    haiku.append("%s %s." % (word_six, word_seven))

    return haiku

if (__name__ == '__main__'):
    print generate_random_lines()
