from gensim.models.word2vec import LineSentence
from gensim.models.word2vec import Text8Corpus
from ms2vec.ms2vec import MultiSense2Vec

corpus = LineSentence("../EVA/text8")
# corpus = Text8Corpus("../EVA/text8", 25)

min_counts = [10, 100, 1000]
min_sense_counts = [100, 1000]
max_sense_num = [2, 3, 5, 10]
np_values = [i/10 for i in range(-5, 6, 1)]
for i in min_counts:
    for j in min_sense_counts:
        if i > j:
            continue
        for s in max_sense_num:
            for np in np_values:
                model = MultiSense2Vec(corpus, sg=1, negative=5, workers=8, iter=5, window=5,
                                       min_count=i, min_sense_count=j, max_sense_num=s,
                                       size=300, np_value=np, cv2zero=True, use_all_window=True, seed=777)

                #print(model.wv.index2word)
                try:
                    print(model.most_similar("mouse"))
                    print(model.most_similar("the"))
                    print(model.most_similar("the--1"))
                except:
                    pass
                model_name = "vectors/npmssg/npmssg_linetext_np"+str(np)+"min"+str(i)+"_minsense"+str(j)+"_maxsensenum"+str(s)+"_cv2zeroTrue_window5True_seed777"
                model.save(model_name)
                model.wv.save_word2vec_format(model_name+".bin", binary=True)
