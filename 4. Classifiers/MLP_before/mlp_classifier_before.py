from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier

def main():
    person = []
    utterance = []
    tags = []
    test_tags=[]
    forward = []
    backward = []
    train = open("train_utterance","r")
    test = open("test_utterance","r")
    train_data = train.readlines()
    test_data = test.readlines()
    for i in range(0,len(train_data)):
        m = train_data[i].strip().split("\t\t")
        utterance.append(m[1])
        n = m[2].split(":")
        tags.append(n[0])
    for i in range(0,len(test_data)):
        m = test_data[i].strip().split("\t\t")
        utterance.append(m[1])
        n = m[2].split(":")
        test_tags.append(n[0])
    
        
    #print(len(utterance), len(tags), len(test_tags))
    vectorizer = TfidfVectorizer()
    X=vectorizer.fit_transform(utterance)
    X.train=X.toarray()
    print("-----------------Data Set is Training----------------------------------------")
    test=[]
    for i in range(703, 865):
        t=X.train[i]
        test.append(t)
    X.train=X.train[0:703]
    mlp = MLPClassifier(hidden_layer_sizes=(100, 50))
    mlp.fit(X.train, tags)
    print("----------------Training Completed---------------------------------------")	
    d=mlp.predict(test)
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
