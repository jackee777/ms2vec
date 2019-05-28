from gensim.models.word2vec import LineSentence
from MS2vec.word2vec import Word2Vec

corpus = LineSentence("test")
model = Word2Vec(corpus)

print(model.most_similar("mouse"))