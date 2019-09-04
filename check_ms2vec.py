from gensim.models.word2vec import LineSentence
from ms2vec.ms2vec import MultiSense2Vec

corpus = LineSentence("enwiki_cleaning.txt")
model = MultiSense2Vec(corpus, sg=1, negative=5, workers=8, iter=5, window=5,
                       min_count=10, min_sense_count=10000, max_sense_num=3,
                       size=300, np_value=-1, cv2zero=True, use_all_window=True, seed=0)

#print(model.wv.index2word)
print(model.most_similar("mouse"))
model_name = "mssg"
model.save(model_name)
model.wv.save_word2vec_format(model_name+".bin", binary=True)
