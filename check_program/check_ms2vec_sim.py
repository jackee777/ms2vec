import gensim

model = gensim.models.KeyedVectors.load_word2vec_format(
    "npmssg_m0.1_enwiki_sense_10_neg_5_min_5000_use_syn1neg.bin", binary = True)

word_list = ["mouse", "announce", "accomplish", "a"]
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