from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
import numpy as np
from sklearn.metrics import accuracy_score

def main():
    person = []
    utterance = []
    tags = []
    test_tags=[]
    forward = []
    backward = []
    temp = []
    train = open("train_data.txt","r")
    test = open("test_data.txt","r")
    train_data = train.readlines()
    test_data = test.readlines()
    for i in range(0,len(train_data)):
        m = train_data[i].strip().split("\t")
        utterance.append(m[1])
        tags.append(m[3])
    print(len(utterance))
    for i in range(0,len(test_data)):
        m = test_data[i].strip().split("\t")
        utterance.append(m[1])
        test_tags.append(m[3])

    print(len(utterance))    
        
    #print(len(utterance), len(tags), len(test_tags))
    vectorizer = TfidfVectorizer()
    X=vectorizer.fit_transform(utterance)
    X.train=X.toarray()
    print("-----------------Data Set is Training----------------------------------------")
    test=[]
    for i in range(394, 497):
        t=X.train[i]
        test.append(t)
    X.train=X.train[0:394]
    mlp = MLPClassifier(hidden_layer_sizes=(70, 35))
    mlp.fit(X.train, tags)
    print("----------------Training Completed---------------------------------------")	
    d=mlp.predict(test)
    accuracy = accuracy_score(test_tags, d)
    print(accuracy)
    count=0
    uncount=0
    for i in range(0,len(d)):
        if(test_tags[i]==d[i]):
            #print(test_tags[i],d[i])
            count+=1
        else:
            uncount+=1
            print(test_tags[i],d[i])
    print(count,uncount)
    
			

if __name__=="__main__":
       main()
