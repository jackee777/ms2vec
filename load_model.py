import numpy as np
data_path = "vec.txt"

def load_model(data_path, binary=0):
    model = {}
    word_list = []
    with open(data_path, "r") as f:
        vocab_size, max_sense, vector_size = f.readline().split()
        for i in f:
            data = i.split()
            word = data[0].split("--")[0]
            vector = np.asarray(data[1:], dtype=np.double)
            if word not in word_list:
                model[word] = vector
                word_list.append(word)
            else:
                model[word] = np.vstack((model[word], vector))
    return model

if __name__ == "__main__":
    model = load_model(data_path)
    print(model["man"])
    print(model["woman"][0] * model["man"][0])
