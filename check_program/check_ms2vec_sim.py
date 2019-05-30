from ms2vec.ms2vec import MultiSense2Vec

model = MultiSense2Vec.load("mssg_text8")
print(model.most_similar("mouse"))