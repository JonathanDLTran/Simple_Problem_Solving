import math
import re
import nltk
from nltk import tokenize
from nltk.stem import PorterStemmer


question = input("Please enter a question: ")

ps = PorterStemmer()

tokenized_question = nltk.word_tokenize(question)
stemmed_question = list(map(lambda word : ps.stem(word), tokenized_question))

print(stemmed_question)

lines_list = tokenize.sent_tokenize(question)

tokenized_lines = list(map(lambda line : nltk.word_tokenize(line), lines_list))

print(tokenized_lines)


# I want to be able to test whether this can solve a physics problem

var_dict = {"v0" : None, "v" : None, "a" : None, "x" : None, "t" : None}




def know_v0_a_t_want_v (v0, a, t):
    return v0 + a * t

def know_v0_v_t_want_x (v0, v, t):
    return (v + v0)/2 * t

def know_v0_a_t_want_x (v0, a, t):
    return v0 * t + 0.5 * a * t * t

def know_v0_a_x_want_v (v0, a, x):
    return math.sqrt(v0 * v0 + 2 * a * x)
