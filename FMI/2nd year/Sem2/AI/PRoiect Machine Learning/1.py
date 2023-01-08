import csv
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
import numpy as np
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV, SGDClassifier
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


#CV = CountVectorizer(lowercase = False, stop_words = None,ngram_range=(1,2),token_pattern = '[a-zA-Z0-9$&+,:;=?@#|<>.^*()%!-]+')
#,token_pattern = '[a-zA-Z0-9$&+,:;=?@#|<>.^*()%!-]+'

CV = TfidfVectorizer(lowercase = False, stop_words = None, ngram_range=(1,2),token_pattern = '[a-zA-Z0-9$&+,:;=?@#|<>.^*()%!-]+')


all_samples_words=train_samples_words+validation_samples_words


sentences_CV = CV.fit_transform(train_samples_words)

#sentences_CV1 = SGDC.fit(train_samples_words)
#.toarray()


#all_CV = CV.fit_transform(all_samples_words)
#.toarray() 
# fit_ttransform sau transform

all_labels_language=train_labels_language+validation_labels_language
all_labels_language=[int(i) for i in all_labels_language]

valid_data=CV.transform(validation_samples_words)
#.toarray()
test_data=CV.transform(test_samples_words)
#.toarray()




#NB2 = LinearDiscriminantAnalysis()
#MLP = MLPClassifier(hidden_layer_sizes=(150,100,50), max_iter=300,activation = 'relu',solver='adam',random_state=1)


#MNB = MultinomialNB(alpha = 0.25)
#, fit_prior = False
#CNB = ComplementNB(alpha = 1.0)
#GNB = GaussianNB()
#LR = LogisticRegression(solver = 'saga')
LR1 = LogisticRegressionCV(solver = 'newton-cg' , max_iter = 20)

#SVC = SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42) 
#svm.SVC()
#LDA =LinearDiscriminantAnalysis()

#NB2 = GaussianNB()

#NB2=RandomForestClassifier()



#CNB.fit(sentences_CV, train_labels_language)

#CNB.fit(all_CV, all_labels_language)
#prediction=CNB.predict(test_data)

#prediction=CNB.predict(valid_data)
#print("CNB : " + str(np.mean(validation_labels_language==prediction)))


#MNB.fit(sentences_CV, train_labels_language)
#prediction1=MNB.predict(valid_data)
#print("MNB : " + str(np.mean(validation_labels_language==prediction1)))



#LR.fit(sentences_CV, train_labels_language)
#prediction2=LR.predict(valid_data)
#print("LR : " + str(np.mean(validation_labels_language==prediction2)))


LR1.fit(sentences_CV, train_labels_language)
prediction3=LR1.predict(valid_data)
print("LR CV : " + str(np.mean(validation_labels_language==prediction3)))



#MNB.fit(all_CV, all_labels_language)
#prediction1=MNB.predict(test_data)

#MLP.fit(sentences_CV, train_labels_language)
#prediction6=MLP.predict(valid_data)
#print("MLP : " + str(np.mean(validation_labels_language==prediction6)))


#GNB.fit(sentences_CV.toarray(), train_labels_language)
#prediction5=MNB.predict(valid_data)
#print("GNB : " + str(np.mean(validation_labels_language==prediction5)))

#SVC.fit(sentences_CV, train_labels_language)
#prediction2=SVC.predict(valid_data)
#print("SVC : " + str(np.mean(validation_labels_language==prediction2)))

#LDA.fit(sentences_CV, train_labels_language)
#prediction3=LDA.predict(valid_data)
#print("LDA : " + str(np.mean(validation_labels_language==prediction3)))


#NB2.fit(all_CV, all_labels_language)

#prediction=NB2.predict(test_data)


#rezultat = pd.DataFrame(data={"id":test_samples_index, "label": prediction1} )
#rezultat.to_csv("./MNB_S10_alpa-0.3-cv-all.csv", index = False)

