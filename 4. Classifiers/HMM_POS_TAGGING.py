def tags():
    file = open("sentence1.txt","r")
    new_file = open("classification.txt","w")
    file_data = file.readlines()
    l = len(file_data)
    tags = []
    person = []
    eng_utter = []
    tel_utter = []
    for i in range(0,l):
        m = file_data[i].strip().split("\t")
        person.append(m[0])
        eng_utter.append(m[1])
        tel_utter.append(m[2])        
        tags.append(m[3])
        new_file.write(m[2]+"/"+m[3]+"\n")
    print(tel_utter)    
        
tags()
        

from __future__ import division #To avoid integer division
from operator import itemgetter
###Training Phase###

file = open("sentence1.txt","r")
file_data = file.readlines()
l = len(file_data)

train_li_words = ['']
train_li_words*= l

train_li_tags = ['']
train_li_tags*= l

for i in range(0,l):
    m = file_data[i].strip().split("\t")
    train_li_words.append(m[2])        
    train_li_tags.append(m[3])

print(train_li_words)
print(train_li_tags)

dict2_tag_follow_tag_ = {}
"""Nested dictionary to store the transition probabilities
each tag A is a key of the outer dictionary
the inner dictionary is the corresponding value
The inner dictionary's key is the tag B following A
and the corresponding value is the number of times B follows A
"""

dict2_word_tag = {}
"""Nested dictionary to store the emission probabilities.
Each word W is a key of the outer dictionary
The inner dictionary is the corresponding value
The inner dictionary's key is the tag A of the word W
and the corresponding value is the number of times A is a tag of W
"""

dict_word_tag_baseline = {}
#Dictionary with word as key and its most frequent tag as value

for i in range(l-1):
    outer_key = train_li_tags[i]
    inner_key = train_li_tags[i+1]
    dict2_tag_follow_tag_[outer_key]=dict2_tag_follow_tag_.get(outer_key,{})
    dict2_tag_follow_tag_[outer_key][inner_key] = dict2_tag_follow_tag_[outer_key].get(inner_key,0)
    dict2_tag_follow_tag_[outer_key][inner_key]+=1

    outer_key = train_li_words[i]
    inner_key = train_li_tags[i]
    dict2_word_tag[outer_key]=dict2_word_tag.get(outer_key,{})
    dict2_word_tag[outer_key][inner_key] = dict2_word_tag[outer_key].get(inner_key,0)
    dict2_word_tag[outer_key][inner_key]+=1


"""The 1st token is indicated by being the 1st word of a senetence, that is the word after period(.)
Adjusting for the fact that the first word of the document is not accounted for that way
"""

dict2_tag_follow_tag_['.'] = dict2_tag_follow_tag_.get('.',{})
dict2_tag_follow_tag_['.'][train_li_tags[0]] = dict2_tag_follow_tag_['.'].get(train_li_tags[0],0)
dict2_tag_follow_tag_['.'][train_li_tags[0]]+=1


last_index = l-1

#Accounting for the last word-tag pair
outer_key = train_li_words[last_index]
inner_key = train_li_tags[last_index]
dict2_word_tag[outer_key]=dict2_word_tag.get(outer_key,{})
dict2_word_tag[outer_key][inner_key] = dict2_word_tag[outer_key].get(inner_key,0)
dict2_word_tag[outer_key][inner_key]+=1


"""Converting counts to probabilities in the two nested dictionaries
& also converting the nested dictionaries to outer dictionary with inner sorted lists
"""
for key in dict2_tag_follow_tag_:
    di = dict2_tag_follow_tag_[key]
    s = sum(di.values())
    for innkey in di:
        di[innkey] /= s
    di = di.items()
    di = sorted(di,key=lambda x: x[0])
    dict2_tag_follow_tag_[key] = di

for key in dict2_word_tag:
    di = dict2_word_tag[key]
    dict_word_tag_baseline[key] = max(di, key=di.get)
    s = sum(di.values())
    for innkey in di:
        di[innkey] /= s
    di = di.items()
    di = sorted(di,key=lambda x: x[0])
    dict2_word_tag[key] = di

#print(dict2_tag_follow_tag_)
#print(dict2_word_tag)

###Testing Phase###    

file = open("sentence1.txt","r")
file_data = file.readlines()
num_words_test = len(file_data)

test_li_words = ['']
test_li_words*= num_words_test

test_li_tags = ['']
test_li_tags*= num_words_test

output_li = ['']
output_li*= num_words_test

output_li_baseline = ['']
output_li_baseline*= num_words_test

num_errors = 0
num_errors_baseline = 0

for i in range(0,num_words_test):
    m = file_data[i].strip().split("\t")
    test_li_words.append(m[2])        
    test_li_tags.append(m[3])

    output_li_baseline[i] = dict_word_tag_baseline.get(m[2],'')
    #If unknown word - tag = 'NNP'
    if output_li_baseline[i]=='':
        output_li_baseline[i]='STATEMENT'
        
        


    if output_li_baseline[i]!=test_li_tags[i]:
        num_errors_baseline+=1

    
    if i==0:    #Accounting for the 1st word in the test document for the Viterbi
        di_transition_probs = dict2_tag_follow_tag_['.']
    else:
        di_transition_probs = dict2_tag_follow_tag_[output_li[i-1]]
        
    di_emission_probs = dict2_word_tag.get(test_li_words[i],'')

    #If unknown word  - tag = 'NNP'
    if di_emission_probs=='':
        output_li[i]='STATEMENT'
        
    else:
        max_prod_prob = 0
        counter_trans = 0
        counter_emis =0
        prod_prob = 0
        while counter_trans < len(di_transition_probs) and counter_emis < len(di_emission_probs):
            tag_tr = di_transition_probs[counter_trans][0]
            tag_em = di_emission_probs[counter_emis][0]
            if tag_tr < tag_em:
                counter_trans+=1
            elif tag_tr > tag_em:
                counter_emis+=1
            else:
                prod_prob = di_transition_probs[counter_trans][1] * di_emission_probs[counter_emis][1]
                if prod_prob > max_prod_prob:
                    max_prod_prob = prod_prob
                    output_li[i] = tag_tr
                    #print "i=",i," and output=",output_li[i]
                counter_trans+=1
                counter_emis+=1    
    

    if output_li[i]=='': #In case there are no matching entries between the transition tags and emission tags, we choose the most frequent emission tag
        output_li[i] = max(di_emission_probs,key=itemgetter(1))[0]  
        
    if output_li[i]!=test_li_tags[i]:
        num_errors+=1

                    
print "Fraction of errors (Baseline) :",(num_errors_baseline/num_words_test)
print "Fraction of errors (Viterbi):",(num_errors/num_words_test)

print "Tags suggested by Baseline Algorithm:", output_li_baseline

print "Tags suggested by Viterbi Algorithm:", output_li

print "Correct tags:",test_li_tags

