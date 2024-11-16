
# Intrusion Detection System (IDS) with Anomaly Detection Model

This project aims to build an Intrusion Detection System (IDS) using machine learning to classify network traffic as either normal or an anomaly. The model uses the NSL-KDD dataset for training and evaluation, which is widely used for testing intrusion detection algorithms.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Contributors](#contributors)

## Project Overview

This project uses the NSL-KDD dataset to train a Random Forest Classifier for detecting network intrusions. The dataset includes network traffic features, with labels indicating whether the traffic is normal or anomalous.

The main objective of this project is to preprocess the data, extract important features, train a machine learning model, and evaluate its performance.

## Dataset

The dataset used in this project is the [NSL-KDD dataset](https://www.kaggle.com/datasets/ashishpatel26/nslkdd) from Kaggle. This dataset is a refined version of the KDD Cup 1999 dataset, addressing some of the inherent issues of the original dataset such as redundant records and class imbalance.

It consists of the following files:
- `KDDTrain+.txt`: The training dataset
- `KDDTest+.txt`: The test dataset
- `kddcup.names`: File containing column names for the datasets

## Requirements

- Python 3.x
- Libraries:
  - pandas
  - numpy
  - sklearn
  - matplotlib
  - joblib
  - scipy

You can install all required libraries using:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/GLCRealm/IDS-with-Anomaly-detection-model.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the NSL-KDD dataset from [Kaggle](https://www.kaggle.com/datasets/ashishpatel26/nslkdd) and place the dataset files (`KDDTrain+.txt`, `KDDTest+.txt`, and `kddcup.names`) in the `dataset/` folder of this repository.

## Usage

### Training the Model

To train the model, run the `IDS_train.ipynb` file. This will:

1. Load the dataset.
2. Preprocess the data by converting categorical variables to binary and creating additional features like protocol attack probabilities.
3. Train a Random Forest classifier using the preprocessed data.
4. Save the trained model as `ebest_model.pkl`.

### Testing the Model

To test the trained model, use the `test_model.py` file. This will:

1. Load the trained model from `ebest_model.pkl`.
2. Preprocess a sample input data.
3. Make predictions on whether the input traffic is normal or an anomaly.

Run the test script with:

```bash
python test_model.py
```

## Model Training

The model is trained using a Random Forest Classifier. Hyperparameter tuning is done via randomized search with cross-validation to find the optimal values for the number of estimators and maximum depth of the tree.

## Model Evaluation

The model is evaluated using the following metrics:
- **Accuracy**: Proportion of correct predictions
- **Precision**: Proportion of true positives among all predicted positives
- **Recall**: Proportion of true positives among all actual positives
- **F1-Score**: Harmonic mean of precision and recall

A confusion matrix is also displayed to evaluate the classification performance.

## Contributors

- [Akash Bhatt](https://github.com/Akash123412)
- [Adarsh Tomar](https://github.com/adarshtomar333)
