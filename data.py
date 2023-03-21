from nltk import sent_tokenize, word_tokenize, pos_tag
import matplotlib.pyplot as plt
import numpy as np

txt = []
tagged = []
POS_TAG = {}

def readFile(file):
    global txt
    txt = open(file,'r').read()

def tag():
    global tagged
    stc_list = sent_tokenize(txt)
    tokenized = [word_tokenize(txt) for txt in stc_list]
    tagged = [pos_tag(txt,tagset="universal") for txt in tokenized]

def analyze():
    global POS_TAG
    count = 0
    for i in range(len(tagged)):
        for a, b in tagged[i]:
            if b != '.':
                if b in POS_TAG.keys():
                    POS_TAG[b] += 1
                else:
                    POS_TAG[b] = 1
    for i in range(len(tagged)):
        for a, b in tagged[i]:
            if b != '.':
                count += 1
    for a, b in POS_TAG.items():
        POS_TAG[a] = b/count
    print(POS_TAG)

def visualize():
    label = list(POS_TAG.keys())
    value = list(POS_TAG.values())
    plt.pie(value, labels = label)
    plt.show() 

def main():
    readFile(input())
    tag()
    analyze()
    visualize()

if __name__ == '__main__':
    main()