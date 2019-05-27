import random

with open("text8", "r") as fr:
    with open("small_text8", "w") as fw:
        for line in fr:
            for l in line.split("\n"):
                print(len(l))