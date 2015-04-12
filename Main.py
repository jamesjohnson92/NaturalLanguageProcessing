from nltk.corpus import names
from nltk.classify import apply_features
import gender_feature
import random
import corpus
import nltk


#variables
train = corpus.train_names
dev = corpus.dev_names
test = corpus.test_names

'''
train_set = apply_features(gender_feature.gender_feature,train)
dev_set = apply_features(gender_feature.gender_feature,dev)
test_set = apply_features(gender_feature.gender_feature,test)

classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier,dev_set)
'''

train_set = [ (gender_feature.gender_feature(n),g) for (n,g) in train ]
dev_set = [ (gender_feature.gender_feature(n),g) for (n,g) in dev]
test_set = [ (gender_feature.gender_feature(n),g) for (n,g) in test]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier,dev_set)

