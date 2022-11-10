import pickle
import os
from word2vec import Word2Vec

if __name__ == "__main__":
    cwd = os.getcwd()

    with open(cwd + '/semantic_expansion/w2v.pkl', 'rb') as input_file:
        w2v = pickle.load(input_file)
    word2expand = input("Word to expand\n")
    w2v.most_similar_words(word2expand, 10)