# KNN Classifier on Iris Dataset

This project implements the **K-Nearest Neighbors (KNN)** algorithm using the **Iris dataset** to classify flower species.

## Dataset
- **Iris dataset** (built-in from `sklearn`)
- Features: Sepal length, Sepal width, Petal length, Petal width  
- Classes: Setosa, Versicolor, Virginica

## Steps Performed
1. Load Iris dataset
2. Split data into training and testing sets
3. Standardize features using `StandardScaler`
4. Train KNN model (`KNeighborsClassifier`)
5. Evaluate using accuracy score and confusion matrix