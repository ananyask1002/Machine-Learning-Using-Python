# Program to display the versions of Python and required Machine Learning libraries used in the experiment.

import sys
print("Python version: {}".format(sys.version))
import pandas as pd
print("pandas version: {}".format(pd.__version__))
import matplotlib
print("matplotlib version: {}".format(matplotlib.__version__))
import numpy as np
print("NumPy version: {}".format(np.__version__))
import scipy as sp
print("SciPy version: {}".format(sp.__version__))
import IPython
print("IPython version: {}".format(IPython.__version__))
import sklearn
print("scikit-learn version: {}".format(sklearn.__version__))
import mglearn
print("mglearn version: {}".format(mglearn.__version__))
---
# This is a small machine learning project for classifying the iris flower and its prediction using four attributes (features) Sepal length, Sepal width, Petal Length, and Petal width.
# Every iris in the dataset belongs to one of three classes, ('setosa' 'versicolor' 'virginica'), so this problem is a three-class classification problem.
# Our goal is to build a machine learning model that can learn from the measurements of these irises whose species is known so that we can predict the species for a new iris.

from sklearn.datasets import load_iris
iris_dataset = load_iris()

# Print all the features present in the iris_dataset
print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))

print(iris_dataset['DESCR'][:193] + "\n...")

print("Target names: {}".format(iris_dataset['target_names']))

print("Feature names: \n{}".format(iris_dataset['feature_names']))

print("Type of data: {}".format(type(iris_dataset['data'])))

print("Shape of data: {}".format(iris_dataset['data'].shape))

print("First five columns of data:\n{}".format(iris_dataset['data'][:5]))

print("Type of target: {}".format(type(iris_dataset['target'])))

print("Shape of target: {}".format(iris_dataset['target'].shape))

print("Target:\n{}".format(iris_dataset['target']))

# Measuring Success: Training and Testing Data (Inputs & outputs) (75% and 25%)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
iris_dataset['data'], iris_dataset['target'], random_state=0)

# Train the data for 75% and test for 25%
print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))

print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))

# Represent the train and test in form of scatter_matrix. Show the result 2D NumPy array of Matplotlib Axes objects.

from pandas.plotting import scatter_matrix

iris_dataframe = pd.DataFrame(
    X_train,
    columns=iris_dataset.feature_names
)

grr = scatter_matrix(
    iris_dataframe,
    c=y_train,
    figsize=(15, 15),
    marker='o',
    hist_kwds={'bins': 20},
    s=60,
    alpha=0.8,
    cmap=mglearn.cm3
)
---
# KNN is a neighbors verification and comparison algorithm which will predict the data accurately.

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

# Fit the model
knn.fit(X_train, y_train)

# Verify the new data
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape: {}".format(X_new.shape))

# Predict the answer
prediction = knn.predict(X_new)
print("Prediction: {}".format(prediction))
print("Predicted target name: {}".format(
iris_dataset['target_names'][prediction]))

# Percentage of accuracy
y_pred = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_pred))

print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))

print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))

X_train, X_test, y_train, y_test = train_test_split(
iris_dataset['data'], iris_dataset['target'], random_state=0)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
