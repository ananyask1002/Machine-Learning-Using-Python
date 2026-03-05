# Unit 1 – Introduction to Machine Learning

## 📌 Overview

Machine Learning (ML) is a branch of Artificial Intelligence that enables computers to learn patterns from data and make predictions without being explicitly programmed. It is widely used in applications such as recommendation systems, fraud detection, image recognition, and predictive analytics.

In this unit, we learn the basic concepts of Machine Learning and implement our first ML model using Python and the Scikit-learn library.

---

## 🎯 Objectives

The main objectives of this unit are:

* To understand the concept of Machine Learning
* To learn the difference between **Supervised** and **Unsupervised Learning**
* To understand the structure of a dataset (samples, features, and labels)
* To learn the Python tools used for Machine Learning
* To build and evaluate a simple ML model

---

## ⚙️ Tools and Libraries Used

| Tool / Library   | Purpose                             |
| ---------------- | ----------------------------------- |
| Python           | Programming language used for ML    |
| NumPy            | Numerical computations and arrays   |
| Pandas           | Data analysis and data manipulation |
| Matplotlib       | Data visualization                  |
| SciPy            | Scientific computing                |
| Scikit-learn     | Machine Learning algorithms         |
| Jupyter Notebook | Interactive coding environment      |

---

## 📊 Dataset Used – Iris Dataset

In this experiment, we use the **Iris dataset**, which is a well-known dataset in Machine Learning.

The dataset contains **150 samples of iris flowers** with the following measurements:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Based on these measurements, the model predicts the **species of the flower**.

### Flower Classes

* Setosa
* Versicolor
* Virginica

Each flower belongs to one of these three classes.

---

## 🧠 Machine Learning Algorithm Used

### K-Nearest Neighbors (KNN)

KNN is a simple and intuitive classification algorithm.

How it works:

1. The algorithm stores the training data.
2. When a new data point is given, it finds the **closest data points (neighbors)** in the training dataset.
3. The new data point is assigned the **most common class among its nearest neighbors**.

---

## 🧪 Procedure

1. Import required Python libraries.
2. Load the Iris dataset using `sklearn.datasets`.
3. Understand dataset structure (features and labels).
4. Split the dataset into:

   * **Training data (75%)**
   * **Testing data (25%)**
5. Create a **KNN classifier model**.
6. Train the model using the training dataset.
7. Make predictions using test data.
8. Evaluate the model using accuracy score.

---

## 📈 Model Evaluation

The model is tested using unseen data (test dataset).
Accuracy is calculated to measure how correctly the model predicts the species of iris flowers.

Example result:

Model Accuracy ≈ **97%**

This means the model correctly predicts the flower species in most cases.

---

## 📌 Key Concepts Learned

* Machine Learning basics
* Supervised Learning
* Classification problems
* Dataset structure (samples, features, labels)
* Training and Testing datasets
* Model evaluation using accuracy

---

## ✅ Conclusion

In this unit, we learned the fundamental concepts of Machine Learning and implemented our first classification model using the **K-Nearest Neighbors (KNN)** algorithm. Using the Iris dataset, we successfully trained and evaluated a machine learning model that can predict flower species based on measurements.

This experiment provides a strong foundation for understanding more advanced machine learning algorithms in upcoming units.

