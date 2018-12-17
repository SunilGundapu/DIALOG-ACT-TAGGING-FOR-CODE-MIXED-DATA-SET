from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier

def classifier():
	labels=[]
	queries=[]
	newlabels=[]
	with open('traindataOriginal','r') as f:
		for l in f:
			a=l.split(':')
			labels.append(a[0])
			queries.append(a[1].rstrip())

	l=[' ','DATE','LOCA','MONE','NUMB','ORGA','PERC','PERS','TIME']
	l2=[' ','DATE','LOCATION','MONEY','NUMB','ORGANIZATION','PERCENT','PERSON','TIME']
 
	for i in labels:
		if(i!='    '):
			newlabels.append(l.index(i))

	#tf-idf vectorization
	vectorizer = TfidfVectorizer()
	X=vectorizer.fit_transform(queries)
	X.train=X.toarray()
	print(X.train)
	#MLP classifier
	t=X.train[len(X.train)-1]
	X.train=X.train[0:1339]
	mlp = MLPClassifier(hidden_layer_sizes=(100, 50))
	mlp.fit(X.train, newlabels)
	print("....Training completed")
	print("\n....Predicting question type")
	test=[]
	test.append(t)
	print(t)
	d=mlp.predict(test)
	print(l2[d[0]])
classifier()
