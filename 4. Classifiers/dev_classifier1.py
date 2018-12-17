from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from collections import Counter
import numpy as arr

def classifier():
       file = open("DATASET/words1.txt","r")
       file1 = open("DATASET/asklib_data.txt","r")
       file_data1 = file1.readlines()
       file_data = file.readlines()
       words = []
       labels = []
       label_no = []
       train_words = []
       test_words = []
       keys = []
       dic ={}
       
       for i in range(0, len(file_data)):
              m=file_data[i].split()
              if(len(m)>0):
                     words.append(m[0])
                     labels.append(m[1])
                     if(m[1]=="univ" or m[1]=="unin" or m[1]=="unit"):
                            label_no.append(0)
                     elif(m[1]=="en" or m[1]=="em" or m[1]=="eb"):
                            label_no.append(1)
                     elif(m[1]=="te"):
                            label_no.append(2)
                     elif(m[1]=="ne"):
                            label_no.append(3)
                     elif(m[1]=="acro"):
                            label_no.append(4)
                     train_words.append(m[0])
   #    print(len(words), len(label_no))
     #  print(set(labels))
       
       for i in range(0, len(file_data1)):
              m=file_data1[i].split()
              if(len(m)>0):
                     words.append(m[0])
                     test_words.append(m[0])       
       unique = Counter(words)
       keys = list(unique.keys())
  
       
       for i in range(0,len(keys)):
              a=[0.0]*9443
              a[i]=1.0
              a=list(a)     
              dic[keys[i]]=a
       print dic['hero']
       input_matrix=[]
       for i in train_words:
              input_matrix.append(dic[i])
     #  print input_matrix
       
	
       #MLP classifier
       mlp = MLPClassifier(hidden_layer_sizes=(100, 50))
       mlp.fit(input_matrix ,label_no)
	
classifier()
