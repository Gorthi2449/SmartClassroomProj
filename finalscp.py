from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
import proj1gui as g
import proj2gui as g1
import proj2 as g2
X=[]
Y=[]
for doc in g2.document:
    X.append(doc[0])
    Y.append(doc[1])
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = LinearSVC().fit(X_train_tfidf, y_train)
while True:
    print('enter your mind')
    input_resp=input()
    if input_resp.lower() == 'bye' or input_resp.lower()=='thank you':
        break
    else:
        res=clf.predict(tfidf_transformer.transform(count_vect.transform([input_resp])))
        if res=='Turn on fan':
            g.res1()
        if res=='Switch on the light':
            g1.res2()
