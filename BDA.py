from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

print("DT")

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier().fit(X_train, y_train)

print("Accuracy:", accuracy_score(y_test, model.predict(X_test)) * 100)

plt.figure(figsize=(12, 8))
plot_tree(model, filled=True)
plt.show()









from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

print("SVM")

X, y = datasets.load_iris(return_X_y=True)
X = X[:, :2]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)

print("Accuracy:",accuracy_score(y_test, model.predict(X_test)) * 100)

h = 0.02
x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1

xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:,0], X[:,1], c=y)

plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.title("Linear SVM")

plt.show()







import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

print("LR")

data = pd.read_csv(r"Admission_P1A.csv")

print(data.head(10))

X = data[['gre', 'gpa', 'rank']]
y = data['admit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Model Accuracy:", round(metrics.accuracy_score(y_test, y_pred), 2))

print("\nEnter student details to predict admission:")

gre = float(input("Enter GRE score: "))
gpa = float(input("Enter GPA: "))
rank = int(input("Enter Rank of Institute (1-4): "))

new_student = pd.DataFrame({'gre':[gre], 'gpa':[gpa], 'rank':[rank]})

prediction = model.predict(new_student)

print("\nEntered Data:")
print(new_student)

if prediction == 1:
    print("Result: Student is likely to be ADMITTED")
else:
    print("Result: Student is NOT likely to be admitted")





import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

print("MLR")

data = pd.read_csv(r"Admission_P1A.csv")
print(data.head())

X = data[['gpa','rank']]
y = data['gre']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model = LinearRegression().fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

print("Mean Absolute Error:", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

gpa = float(input("Enter GPA: "))
rank = int(input("Enter Rank: "))

new = pd.DataFrame({'gpa':[gpa],'rank':[rank]})
print("Predicted GRE Score:", model.predict(new)[0])





import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

print("NB")

data = pd.read_csv(r"spam.csv")

data = data[['Message', 'Category']]
data.columns = ['SMS', 'Type']

cv = CountVectorizer(ngram_range=(1,4), stop_words='english', max_features=1000)
X = cv.fit_transform(data['SMS']).toarray()
y = data['Type']

model = MultinomialNB().fit(X, y)

t1 = cv.transform(['free gifts for all'])
print("free gifts for all:")
print(model.predict(t1))

t2 = cv.transform(['we will go for lunch'])
print("we will go for lunch:")
print(model.predict(t2))




import pandas as pd
import matplotlib.pyplot as mtp

print("KM")

dataset = pd.read_csv (r"Mall_Customers.csv")

x = dataset. iloc[:, [3, 4]] . values
print (x)

from sklearn. cluster import KMeans
wcss_list= [] 

for i in range (1, 11) :
    kmeans = KMeans (n_clusters=i, init='k-means++', random_state= 42)
    kmeans.fit (x)
    wcss_list. append (kmeans. inertia_)
mtp.plot (range (1, 11), wcss_list)
mtp.title ('The Elobw Method Graph')
mtp.xlabel ('Number of clusters (k) ')
mtp.ylabel ('wcss_list')
mtp.show ()

kmeans = KMeans (n_clusters=5, init='k-means++', random_state= 42)
y_predict= kmeans.fit_predict (x)

mtp.scatter (x[y_predict == 0, 0], x[y_predict == 0, 1], s = 100, c = 'blue', label = 'Cluster l') #for first cluster
mtp.scatter (x[y_predict == 1, 0], x[y_predict == 1, 1], s = 100, c = 'green', label = 'Cluster 2') #for second cluster
mtp.scatter (x[y_predict == 2, 0], x[y_predict == 2, 1], s = 100, c = 'red', label = 'Cluster 3') #for third cluster
mtp.scatter (x[y_predict == 3, 0], x[y_predict == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4') #for fourth cluster
mtp.scatter (x[y_predict == 4, 0], x[y_predict == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5') #for fifth cluster
mtp.scatter (kmeans. cluster_centers_[:, 0], kmeans. cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroid' )
mtp.title ('Clusters of customers')
mtp.xlabel ('Annual Income (k$) ')
mtp.ylabel ('Spending Score (1-100) ')
mtp.legend ()
mtp.show ()






















