import gensim

model = gensim.models.KeyedVectors.load_word2vec_format(
    "mssg.bin", binary = True)

word_list = ["mouse", "king", "matrix", "mickey", "couple", "aunt"]
delimiter = "--"
for word in word_list:
    print(word)
    try:
        print(model.most_similar(word))
    except:
        pass
    for i in range(10):
        try:
            print(model.most_similar(word+delimiter+str(i)))
        except:
            pass
    print("\n")