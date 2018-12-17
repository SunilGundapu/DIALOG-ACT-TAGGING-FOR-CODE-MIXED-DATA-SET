from nltk.collocations import BigramCollocationFinder
import re
import codecs
import numpy as np
import string

def main():
       words_all = []
       file = open("DATASET/sentence.txt","r+")
       file_data = file.readlines()
       for i in range(0, len(file_data)):
              if(file_data[i]!="\n"):
                     m = file_data[i].strip().split("\t")
                     words_all.append(m[0]+" "+m[1]+" "+m[2])
       finder = BigramCollocationFinder.from_words(words_all)
       finder.apply_freq_filter(1)
       bigram_model = finder.ngram_fd.viewitems()
       bigram_model = sorted(finder.ngram_fd.viewitems(), key = lambda item : item[1], reverse = True)
       print bigram_model
       np.save("bi-gram.npy",bigram_model)                     
if __name__=="__main__":
       main()
