from gensim.models.word2vec import LineSentence
from ms2vec.ms2vec import MultiSense2Vec

corpus = LineSentence("test")
model = MultiSense2Vec(corpus, sg=1, negative=5, workers=1, iter=1,
                       min_count=1, max_sense_num=3)

#print(model.wv.index2word)
print(model.most_similar("mouse"))