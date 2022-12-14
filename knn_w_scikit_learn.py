# -*- coding: utf-8 -*-
"""KNN w/SciKit Learn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jUdwFOGTY0DVguzaS4-qNbfSlPXqn2Gh

Welcome to the K-Nearest Neighbours model walkthrough!

Made by ***Rodrigo Del Aguila***

The first step is to import the necesasary libraries required to make the KNN model. 

**numpy** provides a multidimensional array object and various pre-made routines for array operations; very useful when working with MNIST dataset. 

**pandas** is a library, similar to Numpy, that contains an efficient dataframe object to be used for data manipulation.

**scikit-learn** is a well-known library used for all kinds of classification, prediction, and machine learning functionalities in general.
"""

import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

"""Now we are able to read, prepare, and normalize the MNIST dataset."""

# reading both training and testing files using pandas
train_df = pd.read_csv('mnist_train.csv')
test_df = pd.read_csv('mnist_test.csv')      

# preparing training data by separating labels from images
y_train = train_df['label']
x_train = train_df.drop(labels=['label'], axis=1)

# preparing testing data by separating labels from images
y_test = test_df['label']
x_test = test_df.drop(labels=['label'], axis=1)

# normalizing data
x_train = x_train / 255.0
x_test = x_test / 255.0

# convert to n-dimensional array
x_train = x_train.values
x_test = x_test.values

"""This next part does not affect the model. It is to show how one can easily make visuals using scikit learn."""

# experimenting with library; using plt (matplotlib.pyplot) module
plt.figure()
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(x_train[i].reshape(28, 28), cmap='gray')
    plt.title(y_train[i])
    plt.axis('off')
    plt.savefig('mnist_plot.png')
plt.show()

"""Now we can find the optimal K value"""

# initializing an array to store accuracy values
acc_list = []
# testing knn classifier with 10 k values by using a loop; variable "i" corresponds to the K value as shown below
for i in range(1, 11):
    knn_classifier = KNeighborsClassifier(n_neighbors=i)
    
    knn_classifier.fit(x_train, y_train)
    
    preds = knn_classifier.predict(x_test)
    
    accuracy = accuracy_score(y_test, preds) * 100
    
    acc_list.append(accuracy)

"""After filling the array with accuracy values, one can find the optimal K value by plotting the relationship between the K value (x-axis) and the %accuracy (y-axis). """

num_k = numpy.arange(1, 11)
plt.figure(dpi=100)
plt.style.use('ggplot')
plt.plot(num_k, acc_list)
plt.xlabel('Number of Neighbors (value of "K")')
plt.ylabel('Accuracy %')
plt.savefig('acc_plot.png')

"""Individually training the model with 3 nearest neighbours."""

# training the model using a K value of 3
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(x_train, y_train)

# making predictions on the test set
preds = knn_classifier.predict(x_test)

print("Accuracy of model at K=3 is",metrics.accuracy_score(y_test, preds)*100)

print("F1 score of model at K=3 is",f1_score(y_test, preds, average='weighted')*100)

"""As a way to analyze the performance of the model, the code below produces a confusion matrix. """

# making a confusion matrix using the metrics module, using accuracies from the optimal K value (K = 3)
# x axis displays predicted label 
# y axis displays true label 
disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, preds)
disp.figure_.suptitle("Confusion Matrix for K = 3")
print(f"Confusion Matrix:\n{disp.confusion_matrix}")

plt.show()

"""**Analysis**
*   The model was able to classify digits with > 97% accuracy
*   The digit that was classified with the most accuracy was **1**, with an error of 0.18%
*   The digit that was classified with the least accuracy was **8**, with an error of 6.56%
*   Average error of 3.11%
*   Exceeds the client's expectation of a minimum 90% accuracy (or maximum 10% error)

"""

import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

# reading both training and testing files using pandas
train_file = pd.read_csv('mnist_train.csv')
test_file = pd.read_csv('mnist_test.csv')

# preparing training data by separating labels from images
y_train = train_file['label']
x_train = train_file.drop(labels=['label'], axis=1)

# preparing testing data by separating labels from images
y_test = test_file['label']
x_test = test_file.drop(labels=['label'], axis=1)

# normalizing data
x_train = x_train / 255.0
x_test = x_test / 255.0

# convert to n-dimensional array
x_train = x_train.values
x_test = x_test.values

A_x_train, B_x_test, A_y_train, B_y_test = train_test_split(x_train, y_train, test_size=0.1, shuffle=False)

#    # initializing an array to store accuracy values
#    acc_list = []
#    # testing knn classifier with 10 k values by using a loop; variable "i" corresponds to the K value as shown below
#    for i in range(1, 11):
#        knn_classifier = KNeighborsClassifier(n_neighbors=i)
#
#        knn_classifier.fit(A_x_train, A_y_train)
#
#        predictions = knn_classifier.predict(B_x_test)
#
#        accuracy = accuracy_score(B_y_test, predictions) * 100
#
#        acc_list.append(accuracy)
#
#    # After filling the array with accuracy values, one can find the optimal K value by plotting the relationship
#    # between the K value (x-axis) and the %accuracy (y-axis).
#    num_k = numpy.arange(1, 11)
#    plt.figure(dpi=100)
#    plt.style.use('ggplot')
#    plt.plot(num_k, acc_list)
#    plt.xlabel('Number of Neighbors (value of "K")')
#    plt.ylabel('Accuracy %')
#    plt.savefig('acc_plot.png')

# training the model using a K value of 3
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(A_x_train, A_y_train)

# making predictions on the test set
predictions = knn_classifier.predict(B_x_test)

print("Accuracy of model at K=3 is", metrics.accuracy_score(B_y_test, predictions)*100)

print("F1 score of model at K=3 is", f1_score(B_y_test, predictions, average='weighted')*100)

# making a confusion matrix using the metrics module, using accuracies from the optimal K value (K = 3)
# x axis displays predicted label
# y axis displays true label
#disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predictions)
#disp.figure_.suptitle("Confusion Matrix for K = 3")
#print("Confusion Matrix:\n{disp.confusion_matrix}")

#plt.show()