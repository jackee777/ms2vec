from gensim.models.word2vec import LineSentence
from ms2vec.ms2vec import Word2Vec

corpus = LineSentence("test")
model = Word2Vec(corpus)

print(model.most_similar("mouse"))