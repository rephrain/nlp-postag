from nltk import sent_tokenize, word_tokenize, pos_tag
import matplotlib.pyplot as plt

# global variabel 
txt = []        # berisi text dalam file txt
tagged = []     # berisi text yang sudah di pisah per kata dan diberi keterangan tiap kata
POS_TAG = {}    # dictionary berisi keterangan yang sudah dihitung jumlahnya kemudian dibagi oleh jumlah seluruh keterangan

# method untuk membaca file txt
def readFile(file): 
    global txt
    txt = open(file,'r').read()

# method untuk memisahkan per kata dari text kemudian diberi keterangan untuk tiap kata
def tag():
    global tagged
    stc_list = sent_tokenize(txt)                                   # list berisi text yang dibagi per kalimat
    tokenized = [word_tokenize(txt) for txt in stc_list]            # list berisi text yang dibagi per kata
    tagged = [pos_tag(txt,tagset="universal") for txt in tokenized] # list tiap kata setelah diberi keterangan

# method untuk menghitung masing masing keterangan kemudian dibagi jumlah seluruh keterangan
def analyze():
    global POS_TAG
    count = 0                           # menghitung jumlah seluruh keterangan
    for i in range(len(tagged)):        # loop untuk list dalam list tagged
        for a, b in tagged[i]:          # loop untuk set dalam list tagged
            if b != '.':                # untuk keterangan '.' di skip
                if b in POS_TAG.keys(): # kalau keterangan berada di dalam dictionary maka jumlah keterangan ditambahkan secara sequential
                    POS_TAG[b] += 1
                else:                   # jika keterangan belum ada dalam dictionary maka set jumlah keterangan dengan 1
                    POS_TAG[b] = 1
    for i in range(len(tagged)):        
        for a, b in tagged[i]:          
            if b != '.':
                count += 1              # menghitung jumlah seluruh keterangan
    for a, b in POS_TAG.items():        # loop untuk POST_TAG dictionary
        POS_TAG[a] = b/count            # jumlah masing masing keterangan dibagi dengan jumlah seluruh keterangan

# method untuk visualisasi data menggunakan pie chart
def visualize():
    label = list(POS_TAG.keys())        # keys dipisahkan dari dictionary menjadi label dalam pie chart
    value = list(POS_TAG.values())      # values dipisahkan dari dictionary menjadi value dalam pie chart
    plt.pie(value, labels = label)
    plt.show() 

def main():
    readFile(input())
    tag()
    analyze()
    visualize()

if __name__ == '__main__':
    main()