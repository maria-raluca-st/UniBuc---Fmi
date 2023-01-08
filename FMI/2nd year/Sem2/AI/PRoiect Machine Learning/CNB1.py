import csv
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

import pandas as pd


def read_from_file(storage1, storage2, filename, encoding, delimiter="\t"):
    f = open(filename, encoding=encoding)
    text = csv.reader(f, delimiter=delimiter)
    for elem in text:
        storage1.append(int(elem[0]))
        storage2.append(elem[1])

def read_from_file_csv(storage1, storage2, filename, encoding, delimiter="\t"):
    f = open(filename, encoding=encoding)
    text = csv.reader(f, delimiter=delimiter)
    for elem in text:
        storage1.append(elem[0])
        storage2.append(elem[1])

train_samples_index = []
train_samples_words = []
train_labels_index = []
train_labels_language = []
test_samples_index=[]
test_samples_words=[]
validation_samples_words = []
validation_samples_index=[]
validation_labels_index=[]
validation_labels_language=[]

sub_labels_index = []
sub_labels_language = []

read_from_file( train_samples_index, train_samples_words, "train_samples.txt", "mbcs")
read_from_file(train_labels_index, train_labels_language, "train_labels.txt", "utf-8")
read_from_file(test_samples_index, test_samples_words, "test_samples.txt", "mbcs")
read_from_file(validation_labels_index, validation_labels_language, "validation_labels.txt", "utf-8")
read_from_file(validation_samples_index, validation_samples_words, "validation_samples.txt", "mbcs")
read_from_file_csv(sub_labels_index, sub_labels_language, "sample_submission.txt", "mbcs",",")


train_labels_language = [int(i) for i in train_labels_language]
validation_labels_language=[int(i) for i in validation_labels_language]
sub_labels_language=sub_labels_language[1:]
sub_labels_index=sub_labels_index[1:]


CV = CountVectorizer(lowercase = False, stop_words = None,ngram_range=(1,2),token_pattern = '[a-zA-Z0-9$&+,:;=?@#|<>.^*()%!-]+')
#,token_pattern = '[a-zA-Z0-9$&+,:;=?@#|<>.^*()%!-]+'
#CV = TfidfVectorizer(lowercase = False, stop_words = None, smooth_idf = False, ngram_range=(1,2),max_features=25000)


all_samples_words=train_samples_words+validation_samples_words


#sentences_CV = CV.fit_transform(train_samples_words)
#.toarray()

all_CV = CV.fit_transform(all_samples_words)
#.toarray() # fit_ttransform sau transform

all_labels_language=train_labels_language+validation_labels_language
all_labels_language=[int(i) for i in all_labels_language]

valid_data=CV.transform(validation_samples_words)
#.toarray()
test_data=CV.transform(test_samples_words)
#.toarray()




#NB2 = LinearDiscriminantAnalysis()
#NB2 = MLPClassifier(hidden_layer_sizes=(10,50), max_iter=200,activation = 'relu',solver='adam',learning_rate_init=0.001)

#NB2 = MultinomialNB(alpha = 0.3)
NB2 = ComplementNB()
#NB2 = svm.SVC()
#NB2 = GaussianNB()

#NB2=RandomForestClassifier()



#NB2.fit(sentences_CV, train_labels_language)
NB2.fit(all_CV, all_labels_language)


prediction=NB2.predict(test_data)
#prediction=NB2.predict(valid_data)


#print(np.mean(validation_labels_language==prediction))


rezultat = pd.DataFrame(data={"id":test_samples_index, "label": prediction} )
rezultat.to_csv("./CNB_S1.csv", index = False)

