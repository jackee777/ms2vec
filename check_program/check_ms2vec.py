from gensim.models.word2vec import LineSentence
from ms2vec.ms2vec import MultiSense2Vec

corpus = LineSentence("../enwiki_cleaning.txt")
model = MultiSense2Vec(corpus, sg=1, negative=5, workers=4, iter=5,
                       min_count=10, min_sense_count=4000, max_sense_num=3)

#print(model.wv.index2word)
print(model.most_similar("mouse"))
model_name = "mssg_enwiki_sense_3_neg_5_use_syn1neg"
model.save(model_name)
model.wv.save_word2vec_format(model_name+".bin", binary=True)
