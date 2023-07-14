import os
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def handler(event, context):
    # Load the Iris dataset
    dataset = datasets.load_iris()
    X = dataset.data
    y = dataset.target

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize a Random Forest classifier
    clf = RandomForestClassifier()

    # Train the classifier
    clf.fit(X_train, y_train)

    # Use the trained classifier to make predictions on the test set
    y_pred = clf.predict(X_test)

    # Compute the accuracy of the classifier
    accuracy = accuracy_score(y_test, y_pred)

    # Compute the confusion matrix
    confusion = confusion_matrix(y_test, y_pred)

    # Return the accuracy and confusion matrix
    return {
        'accuracy': accuracy,
        'confusion_matrix': confusion.tolist()
    }
