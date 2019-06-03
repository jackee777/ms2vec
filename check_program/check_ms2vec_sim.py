import gensim

model = gensim.models.KeyedVectors.load_word2vec_format(
    "mssg_enwiki_sense_3_neg_5_min_10000_use_syn1neg.bin", binary = True)

word_list = ["mouse", "announce", "accomplish"]
delimiter = "--"
for word in word_list:
    print(word)
    print(model.most_similar(word))
    for i in range(3):
        try:
            print(model.most_similar(word+delimiter+str(i)))
        except:
            pass
    print("\n")