from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec

#corpus = LineSentence("text8")
#model = Word2Vec(corpus)

#print(model.most_similar("mouse"))

class test(object):
    """
    zip(iter1 [,iter2 [...]]) --> zip object

    Return a zip object whose .__next__() method returns a tuple where
    the i-th element comes from the i-th iterable argument.  The .__next__()
    method continues until the shortest iterable in the argument sequence
    is exhausted and then it raises StopIteration.
    """

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, iter1, iter2=None, *some):  # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs):  # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs):  # real signature unknown
        """ Implement next(self). """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        """ Return state information for pickling. """
        pass

L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in test(*L):
    print(i)