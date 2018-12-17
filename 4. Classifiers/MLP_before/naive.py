import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import DecisionTreeClassifier
from textblob.classifiers import MaxEntClassifier
from textblob import TextBlob

train = []
test = []
temp = ()

file1 = open("train_utterance","r")
file_data = file1.readlines()
for i in range(0,len(file_data)):
    m = file_data[i].strip().split("\t\t")
    n = m[2].split(":")
    temp = (m[1],n[0])
    train.append(temp)
file1.close()

    
file1 = open("test_utterance","r")
file_data = file1.readlines()
for i in range(0,len(file_data)):
    m = file_data[i].strip().split("\t\t")
    n = m[2].split(":")
    temp = (m[1],n[0])
    test.append(temp)

cl = NaiveBayesClassifier(train)
mec = MaxEntClassifier(train)
#dtc = DecisionTreeClassifier(train)

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))
print("Accuracy: {0}".format(mec.accuracy(test)))

# Show 5 most informative features
cl.show_informative_features(5)
