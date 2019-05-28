from gensim.models.word2vec import LineSentence
from ms2vec.ms2vec import MultiSense2Vec

corpus = LineSentence("test")
model = MultiSense2Vec(corpus, max_sense_num=3)

print(model.most_similar("mouse"))