from typing import List
import gensim.downloader
import numpy as np
import pickle
import os


def get_similarity(v1: np.ndarray, v2:np.ndarray):
    '''
    Input:
    - v1: embedding for word 1
    - v2: embedding for word 2

    Return:
    - similarity: cosine similarity between v1 and v2
    '''
    similarity = None
    # TODO: calculate similarity between v1 and v2
    similarity = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return similarity


class Word2Vec():
    """word2vec embeddings."""

    def __init__(self, embed, matrix, index_to_key, key_to_index):
        self.embed = embed
        self.matrix = matrix
        self.index_to_key = index_to_key
        self.key_to_index = key_to_index

    def most_similar_words(self, word: str, topk: int):
        '''
        Input:
        - vector: query vector
        - topk: top k words

        Return:
        - None: print out the top k similar words and similarities
        '''
        # TODO: print out topk most similar words and their probabilities
        vector = self.embed[word]
        vector = vector/np.linalg.norm(vector)
        score = np.matmul(self.matrix, vector)
        k_ind = np.argpartition(score, -topk)[-topk:]
        k_ind = k_ind[np.argsort(-score[k_ind])]

        print("topk words and corresponding similarities are:")
        for idx in k_ind:
            print(np.array(self.index_to_key)[idx], score[idx])
        pass

if __name__ == "__main__":
    cwd = os.getcwd()
    embed = gensim.downloader.load('glove-wiki-gigaword-300')
    matrix = embed.get_normed_vectors()
    word2vec = Word2Vec(embed, matrix, embed.index_to_key, embed.key_to_index)
    with open(cwd+'/semantic_expansion/w2v.pkl', 'wb') as out:
        pickle.dump(word2vec, out, pickle.HIGHEST_PROTOCOL)

    # word2expand = input("Word to expand\n")
    # word2vec.most_similar_words(word2expand, 10)