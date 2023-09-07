# Predicting Electricity Consumption of a Building using Scikit-learn

This Jupyter notebook demonstrates how to predict the electricity consumption of a building using Scikit-learn, a popular machine learning library in Python.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Data Import](#data-import)
4. [Data Preprocessing](#data-preprocessing)
5. [Model Building](#model-building)
6. [Evaluation](#evaluation)
7. [Conclusion](#conclusion)

## 1. Introduction <a name="introduction"></a>

This notebook focuses on using machine learning to predict electricity consumption in a building. It utilizes the Scikit-learn library and follows a structured approach to tackle this problem.

## 2. Setup <a name="setup"></a>

Before getting started, make sure you have the necessary libraries installed. We'll use Numpy, Pandas, and Scikit-learn for this project.

```python
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
```

## 3. Data Import <a name="data-import"></a>
In this section, we import the building dataset based on geographical location and usage interactively. Additionally, we import a metadata file to provide context about the buildings in the dataset.

```python
metadata = pd.read_csv("data/meta_open.csv")
```
## 4. Data Preprocessing <a name="data-preprocessing"></a>
Data preprocessing is a crucial step in machine learning. In this section, we clean and prepare the data for modeling. This includes handling missing values, feature engineering, and splitting the data into training and testing sets.

## 5. Model Building <a name="model-building"></a>
We employ a K-Nearest Neighbors (KNN) regression model to predict electricity consumption. KNN is a simple and effective algorithm for regression tasks. We train the model on the training data and make predictions.

## 6. Evaluation <a name="evaluation"></a>
To assess the model's performance, we evaluate it using appropriate metrics such as Mean Absolute Error (MAE) or Root Mean Square Error (RMSE). This section provides insights into how well the model predicts electricity consumption.

## 7. Conclusion <a name="conclusion"></a>
In conclusion, this Jupyter notebook demonstrates the process of predicting electricity consumption in a building using Scikit-learn. It covers data import, preprocessing, model building, and evaluation. You can adapt this methodology to similar predictive modeling tasks in the field of energy consumption analysis.

