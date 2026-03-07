# 📘 Unit 3 – Supervised Learning – 2

## 📌 Introduction

In this unit, we explore several powerful supervised machine learning algorithms that are widely used for classification and prediction tasks. These models include **Naive Bayes classifiers**, **Decision Trees**, and advanced **ensemble learning methods** such as **Random Forest** and **Gradient Boosting**.

These algorithms help machines learn patterns from data and make accurate predictions. They are commonly applied in areas such as **text classification, medical diagnosis, fraud detection, recommendation systems, and predictive analytics**.

---

## 🧠 Naive Bayes Classifiers

Naive Bayes is a **probabilistic machine learning algorithm** based on **Bayes’ Theorem**. It assumes that the features used for prediction are independent of each other, which simplifies the learning process and makes the algorithm very fast.

Naive Bayes classifiers are especially useful for **large datasets and high-dimensional data**.

Types of Naive Bayes include:

* **Gaussian Naive Bayes** – Used for continuous numerical data
* **Bernoulli Naive Bayes** – Used for binary features
* **Multinomial Naive Bayes** – Commonly used in text classification

Naive Bayes models are simple, efficient, and often used as **baseline models in machine learning**.

---

## 🌳 Decision Trees

Decision Trees are one of the most intuitive machine learning algorithms. They make predictions by learning a series of **if–else decision rules** that split the dataset into smaller groups.

Each split is based on a feature that best separates the data into different classes or values.

Key advantages of decision trees include:

* Easy to understand and interpret
* Works with both numerical and categorical data
* No need for feature scaling
* Can model complex relationships between variables

However, if a decision tree becomes too complex, it may **overfit the training data**. Techniques like limiting the depth of the tree or controlling the number of samples in each node help reduce this problem.

---

## 📊 Feature Importance

Decision tree models can measure the **importance of each feature** used in prediction.

Feature importance helps us understand:

* Which variables influence the model the most
* How the model makes decisions
* Which features are most useful for prediction

The importance values range from **0 to 1**, and the total importance across all features equals **1**.

---

## 🤖 Ensemble Methods

Ensemble learning improves machine learning performance by **combining multiple models** instead of relying on a single model.

By combining many models together, ensemble methods can produce **more accurate and stable predictions**.

Two important ensemble techniques discussed in this unit are **Random Forest** and **Gradient Boosting**.

---

## 🌲 Random Forest

Random Forest is an ensemble algorithm that builds **many decision trees** and combines their predictions.

Each tree is trained on a **random subset of the data and features**, which helps reduce overfitting and improves model accuracy.

Key advantages of Random Forest include:

* Higher accuracy compared to a single decision tree
* Reduced overfitting
* Works well on large datasets
* Handles complex data relationships

The final prediction is obtained by **majority voting for classification** or **averaging for regression**.

---

## ⚡ Gradient Boosting

Gradient Boosting is another powerful ensemble technique. Unlike Random Forest, it builds trees **sequentially**, where each new tree tries to correct the mistakes made by the previous trees.

The model gradually improves its performance by focusing on difficult examples in the dataset.

Important parameters in Gradient Boosting include:

* **n_estimators** – Number of trees in the model
* **learning_rate** – Controls how strongly each tree influences the model
* **max_depth** – Limits the complexity of each tree

Gradient Boosting models are widely used in **industry applications and machine learning competitions** because of their strong predictive performance.

---

## 📊 Applications

The algorithms covered in this unit are widely used in many real-world applications, including:

* Email spam detection
* Medical diagnosis systems
* Credit risk and fraud detection
* Customer behavior prediction
* Recommendation systems

---

## 📚 Conclusion

This unit introduces several important machine learning techniques used for predictive modeling. **Naive Bayes** provides a fast and simple probabilistic approach, **Decision Trees** offer interpretability and structured decision-making, and **Ensemble Methods** like **Random Forest** and **Gradient Boosting** significantly improve model performance.

Understanding these algorithms helps build a strong foundation for solving real-world machine learning problems and developing intelligent data-driven systems.

