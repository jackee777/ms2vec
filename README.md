# ms2vec
This is a python package for MSSG and NP-MSSG by Neelakantan. I already checked the score in SimLex-999 and that is almost same in the article.

Perhaps, I can response issuses until 2019/03/31 when I will get Master's degree.

The original information is like this.
### NP-MSSG
the code from research paper ["Efficient Non-parametric Estimation of Multiple Embeddings per Word in Vector Space"](http://arxiv.org/pdf/1504.06654v1.pdf) by Arvind Neelakantan, Jeevan Shankar, Alexandre Passos, Andrew McCallum


1. the code provided by the authors of the paper. I took the code from [bitbucket account] (https://bitbucket.org/jeevan_shankar/multi-sense-skipgram/src/74aeafd22528710cd60c72d6d1d0c0edad37f567?at=master.),
2. to download the vectors trained by the provided method, follow the [link](http://iesl.cs.umass.edu/downloads/vectors/release.tar.gz), archive size is 3.3Gb 

### github page
https://github.com/yauhen-info/NP-MSSG#np-mssg


# how to use
This code is available in the same way as gensim because this program is the extenion of gensim 3.7.2. 

However, the learning method of this program skip-gram and negative sampling only. Other combinations don't work.

## MSSG
MSSG is executed if np-value is -1.
```angular2html
from gensim.models.word2vec import LineSentence
from ms2vec.ms2vec import MultiSense2Vec

corpus = LineSentence("your_corpus")
model = MultiSense2Vec(corpus, sg=1, negative=5, workers=4, iter=5, window=5,
                       min_count=10, min_sense_count=5000, max_sense_num=3,
                       size=300, np_value=-1 ,seed=777)

model_name = "mssg_model"
model.save(model_name)
# bin format is available in gensim's KeyedVectors
model.wv.save_word2vec_format(model_name+".bin", binary=True)
```

## NP-MSSG
NP-MSSG is executed if np-value is not -1.
```angular2html
from gensim.models.word2vec import LineSentence
from ms2vec.ms2vec import MultiSense2Vec

corpus = LineSentence("your_corpus")
model = MultiSense2Vec(corpus, sg=1, negative=5, workers=4, iter=5, window=5,
                       min_count=10, min_sense_count=5000, max_sense_num=10,
                       size=300, np_value=-0.5 ,seed=777)

model_name = "npmssg_model"
model.save(model_name)
# bin format is available in gensim's KeyedVectors
model.wv.save_word2vec_format(model_name+".bin", binary=True)
```


# Thank you for reading
I hope that this program works well and word embedding can contribute into NLP.

If this program is helpful for you, I want you to give the star this program for me.
Have a nice day.
