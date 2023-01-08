import csv
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics import confusion_matrix 
from sklearn.naive_bayes import  MultinomialNB

# librarie pentru DataFrame , proceseaza datele rapid
import polars as pl

# modul pentru regular expression
import re


ts = csv.reader(open("train_samples.txt", encoding= "mbcs"), delimiter= "\t")
ts_id = []
ts_data = []
for l in ts:
    ts_id.append(int(l[0]))
    ts_data.append(l[1])
   
tl = csv.reader(open("train_labels.txt"), delimiter= "\t")
tl_id = []
tl_class = []
for l in tl:
     tl_id.append(int(l[0]))
     tl_class.append(int(l[1]))

vs = csv.reader(open("validation_samples.txt", encoding= "mbcs"), delimiter= "\t")
vs_id=[]
vs_data = []
for l in vs:
     vs_id.append(int(l[0]))
     vs_data.append(l[1])

vl = csv.reader(open("validation_labels.txt"), delimiter= "\t")
vl_id=[]
vl_class=[]
for l in vl:
    vl_id.append(int(l[0]))
    vl_class.append(int(l[1]))

tests = csv.reader(open("test_samples.txt", encoding= "mbcs"), delimiter= "\t")
test_id = []
test_data = []
for l in tests:
    test_id.append(int(l[0]))
    test_data.append(l[1])


def tok(data):
    # split data doar pe whitespace , ca sa prevenim CountVectorizer din a ignora punctuatie + caractere speciale la tokenizing
    return re.split("\\s+",data)

# CV pentru preprocesarea datelor + implementarea Bag of Words

CV = CountVectorizer(lowercase = False , ngram_range=(1,2),tokenizer = tok)
#,token_pattern = '[a-zA-Z0-9$&+,:;=?@#|<>.^*()%!-]+'

#matricea pt train
train_vector = CV.fit_transform(ts_data)
#.toarray()


# matricea pt testare
valid_d=CV.transform(vs_data)
#.toarray()


MNB = MultinomialNB(alpha = 0.3)

# antrenarea
MNB.fit(train_vector, tl_class)

# testam modelul pe valid data
pred = MNB.predict(valid_d)


print("Acuratete MNB : " + str(np.mean(pred == vl_class)))

print("Matrice acuratete : \n")
print(confusion_matrix(vl_class , pred ))



#df = pl.DataFrame(data={"id" : test_id, "label": prediction1})
#df.to_csv("./MNB_S11_alpha_0.3_cv.csv")
