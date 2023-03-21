from nltk import sent_tokenize, word_tokenize, pos_tag

txt = []

def readFile (file):
    global txt
    txt = open(file,'r').read()

def tag ():
    stc_list = sent_tokenize(txt)
    tokenized = [word_tokenize(txt) for txt in stc_list]
    tagged = [pos_tag(txt,tagset="universal") for txt in tokenized]

def main():
    readFile(input())