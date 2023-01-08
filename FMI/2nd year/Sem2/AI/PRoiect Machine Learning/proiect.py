import pandas as pd # pt data frames
import numpy as np  # aritmetica + arrays
import collections  # pt dictionare
import csv

from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier 

from sklearn.model_selection import train_test_split # pt split data in samples de  training si testing
from sklearn.decomposition import PCA # Principal component analysis used to reduce the number of features in a model
from sklearn.preprocessing import StandardScaler # used to scale data to be used in the model

from sklearn import metrics # pt acuratete
from sklearn.metrics import confusion_matrix,classification_report,roc_auc_score,roc_curve,accuracy_score,log_loss

from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer

import pickle # pt save model antrenat + citirea lui

import seaborn as sns #plots
sns.set(style="ticks")
import matplotlib.pyplot as plt # Create plots


np.random.seed(500)  #used to reproduce the same result every time if the script is kept consistent 



def read1(filename, encoding,storage1, storage2):
    f = open(filename, encoding=encoding)
    text = csv.reader(f, delimiter = "\t")
    
    storage1 = []
    storage2 = []
    for elem in text:
        storage1.append(int(elem[0]))
        storage2.append(elem[1])


def read_samples(path, encoding):
    ids = [] 
    data = []   # id-urile + propozitiile in sine
    f = open(path,'r', encoding=encoding)
    while f.readline():
        d = f.readline().split('\t')  # datele sunt delimitate de tabs
        #print(d)
        ids.append(d[0])
        data.append(d[1:])
    return ids,data


def read_labels(path, encoding):
    id_limba = [] 
    label_id = []   # id-urile + propozitiile in sine
    f = open(path,'r', encoding=encoding)
    while f.readline():
        d = f.readline().split('\t')  # datele sunt delimitate de tabs
        id_limba.append(d[0])
        label_id.append(d[1:])
    return id_limba,label_id


train_s_index =[]
train_s_words =[]

read1("train_samples.txt", "mbcs" , train_s_index,train_s_words)
#train_s_index,train_s_words = read_samples("train_samples.txt", "mbcs")
#train_s_words = [str(train_s_words)]
print(train_s_words)


train_labels = read_labels("train_labels.txt", "utf-8")
train_l_index = train_labels[0]
train_l_language = train_labels[1]




validation_data = read_samples("validation_samples.txt", "mbcs")
validation_s_words = validation_data[0]
validation_s_index= validation_data[1]



validation_labels = read_labels("validation_labels.txt", "utf-8")
validation_l_index= validation_labels[0]
validation_l_language= validation_labels[1]


test_data = read_samples("test_samples.txt", "mbcs")
test_s_index= test_data[0]
test_s_words= test_data[1]

# Count Vectorizer - separa cuvintele si le da un ID(int) + le numara aparitiile 
# lowercase = False - Count Vectorizer converteste automat cuvintele cu majuscula in litere mici 
# dar noi nu stim care sunt regulile din limbajele 1,2,3 , deci nu vrem transformarea 
# token_pattern ->  Spunem cu regex sa nu ignore caractere speciale , ceea ce altfel face automat
# stop_words = None -> nu stim care sunt cele mai folosite cuvinte din limba , deci setam None
CV = CountVectorizer(lowercase = False, token_pattern = '[a-zA-Z0-9$&+,:;=?@#|<>.^*()%!-]+' , stop_words = None,ngram_range=(1,2),max_features=25000)


# preprocesarea datelor
sentences_CV = CV.fit_transform(train_s_words)
#.toarray()


valid_data=CV.transform(validation_s_words)
#.toarray()
test_data=CV.transform(test_s_words)
#.toarray()


NB2 = MultinomialNB(alpha = 0.5)

# antrenarea datelor
NB2.fit(sentences_CV, train_l_language)

# testarea 
prediction=NB2.predict(valid_data)

# acuratetea
print(np.mean(validation_labels_language==prediction))

