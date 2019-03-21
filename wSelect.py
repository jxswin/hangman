import random

#to generate a random word from .txt file

def generate_the_word(infile):
    random_line = random.choice(open(infile).read().split('\n'))
    return random_line

def get_word():
    infile = "words.txt"
    return(generate_the_word(infile))
