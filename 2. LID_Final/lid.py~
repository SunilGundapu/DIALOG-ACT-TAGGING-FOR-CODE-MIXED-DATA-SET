import nltk
import sklearn_crfsuite
import pycrfsuite
import itertools
import numpy as np
from sklearn.metrics import classification_report

file = open('code_mixed_train')
file_data = file.readlines()
file1 = open('code_mixed_test')
file_data1 = file1.readlines()
train_data = []
train = []
test_data = []
test = []
for i in range(0,len(file_data)):
       if(len(file_data[i].split())>0):       
              m = tuple(file_data[i].split())
              train.append(m)
       else:
              train_data.append(train)
              train = []
for i in range(0,len(file_data1)):
       if(len(file_data1[i].split())>0):       
              m = tuple(file_data1[i].split())
              test.append(m)
       else:
              test_data.append(test)
              test = []

#print(train_data[0])
#print(test_data[0])

def word2features(sent, i):
    #print(sent,i)
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

def sent2tokens(sent):
    return [token for token, postag, label in sent]

X_train = [sent2features(s) for s in train_data]
y_train = [sent2labels(s) for s in train_data]

X_test = [sent2features(s) for s in test_data]
y_test = [sent2labels(s) for s in test_data]

trainer = pycrfsuite.Trainer(verbose=True)

# Submit training data to the trainer
for xseq, yseq in zip(X_train, y_train):
    trainer.append(xseq, yseq)

# Set the parameters of the model
trainer.set_params({
    # coefficient for L1 penalty
    'c1': 0.1,

    # coefficient for L2 penalty
    'c2': 0.01,  

    # maximum number of iterations
    'max_iterations': 200,

    # whether to include transitions that
    # are possible, but not observed
    'feature.possible_transitions': True
})

# Provide a file name as a parameter to the train function, such that
# the model will be saved to the file when training is finished
trainer.train('crf.model')

tagger = pycrfsuite.Tagger()
tagger.open('crf.model')
y_pred = [tagger.tag(xseq) for xseq in X_test]

# Let's take a look at a random sample in the testing set
'''
For Manual Calculations
y_test = list(itertools.chain.from_iterable(y_test))
y_pred = list(itertools.chain.from_iterable(y_pred))

count=0

for i in range(len(y_test)):
    if(y_test[i]==y_pred[i]):
        count+=1

print(len(y_test),count)
'''


# Create a mapping of labels to indices
labels = {'univ':0, 'te':1, 'en':2, 'ne':3}

# Convert the sequences of tags into a 1-dimensional array

predictions = np.array([labels[tag] for row in y_pred for tag in row])
truths = np.array([labels[tag] for row in y_test for tag in row])

# Print out the classification report
print(classification_report(
    truths, predictions,
    target_names=['univ', 'te', 'en', 'ne']))
    

