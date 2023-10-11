"""
@author: TYZ
CSE258 homework1.py
"""

# import packages
import json
from collections import defaultdict
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import numpy as np
import random
import gzip
import dateutil.parser
import math

# generate answer


answers = {}


# check if content type is correct


def assertFloat(x):
    assert type(float(x)) == float


def assertFloatList(items, N):
    assert len(items) == N
    assert [type(float(x)) for x in items] == [float]*N


# Question 1
# dealing with files


f = gzip.open("fantasy_10000.json.gz")
dataset = []
for content in f:
    dataset.append(json.loads(content))

sums = 0
for i in dataset:
    if 'review_text' in i.keys():
        sums = sums + 1

# check if all dict has 'review_text' to prevent exceptions
assert sums == len(dataset)


# extract the feature vector of one line of data
def feature(datum):
    """
    :param: datum : one line of dataset(a dictionary)
    :return: a parsed feature only contains length of 'review_text'
             and one additional dimension of 1
    """

    return [1, len(datum['review_text'])]


# calculate feature vector and target vector
X = [feature(content) for content in dataset]
Y = [content['rating'] for content in dataset]


# transform X, Y to np.array for convenience
X = np.array(X)
Y = np.array(Y)


# calculate the unknown params(theta) in linear regression
# theta = (X X^T)^{-1} X^T Y
theta = np.matmul(np.linalg.inv(np.matmul(np.transpose(X), X)), np.transpose(X))
theta = np.matmul(theta, Y)
theta = theta.tolist()


# calculate mean square error, record in answer dictionary
MSE = mean_squared_error(np.matmul(X, theta), Y)
answers['Q1'] = [theta[0], theta[1], MSE]


# check for data type
assertFloatList(answers['Q1'], 3)


# Question 2


# parse date and put the parsed_date to dataset
for d in dataset:
    t = dateutil.parser.parse(d['date_added'])
    d['parsed_date'] = t


# new feature extractor function
def feature(datum):
    """
    :param: datum: a single line of parsed_dataset including the parsed date information
    :return: one hot encoding of week time and month time.
    """

    week_encoding = np.zeros(6)
    month_encoding = np.zeros(11)
    month_number = datum['parsed_date'].month
    week_number = datum['parsed_date'].weekday()
    if month_number != 1:
        month_encoding[month_number - 2] = 1
    if week_number != 0:
        week_encoding[week_number - 1] = 1

    result = np.concatenate((np.array([1, len(datum['review_text'])]), week_encoding, month_encoding))

    return result


# extract features
X = [feature(content) for content in dataset]
Y = [content['rating'] for content in dataset]
X = np.array(X)
Y = np.array(Y)


# record and check for answers of Q2
answers['Q2'] = [X[0], X[1]]

assertFloatList(answers['Q2'][0], 19)
assertFloatList(answers['Q2'][1], 19)


# Question3


# new feature extractor
def feature3(datum):
    """
    :param: datum: parsed_dataset including the parsed date information
    :return: easy encoding of week time and month time.
    """

    week_number = datum['parsed_date'].weekday()
    month_number = datum['parsed_date'].month

    result = np.array([1, len(datum['review_text']), week_number, month_number])

    return result


# extract features and record in X3, Y3. Then transform them to np.array
X3 = [feature3(content) for content in dataset]
Y3 = [content['rating'] for content in dataset]
X3 = np.array(X3)
Y3 = np.array(Y3)


# calculate both unknown params of each model. referring to theta2 and theta3
# theta2 is the params of one-hot encoding, theta3 is the params of simple encoding
theta3 = np.matmul(np.linalg.inv(np.matmul(np.transpose(X3), X3)), np.transpose(X3))
theta3 = np.matmul(theta3, Y3)
theta2 = np.matmul(np.linalg.inv(np.matmul(np.transpose(X), X)), np.transpose(X))
theta2 = np.matmul(theta2, Y)


# evaluation result using mean square error, then record them to ans{}
mse2 = mean_squared_error(np.matmul(X, theta2), Y)
mse3 = mean_squared_error(np.matmul(X3, theta3), Y)
answers['Q3'] = [mse2, mse3]
assertFloatList(answers['Q3'], 2)


# Question 4


# shuffling the dataset randomly using the random seed 0, then extract features
random.seed(0)
random.shuffle(dataset)
X2 = [feature(content) for content in dataset]
X3 = [feature3(content) for content in dataset]
Y = [d['rating'] for d in dataset]


# split the features into training dataset and testing dataset, both containing
# non-overlapping half data of the original dataset
train2, test2 = X2[:len(X2)//2], X2[len(X2)//2:]
train3, test3 = X3[:len(X3)//2], X3[len(X3)//2:]
trainY, testY = Y[:len(Y)//2], Y[len(Y)//2:]
train2 = np.array(train2)
train3 = np.array(train3)
test2 = np.array(test2)
test3 = np.array(test3)
trainY = np.array(trainY)
testY = np.array(testY)


# calculate theta
theta2 = np.matmul(np.linalg.inv(np.matmul(np.transpose(train2), train2)), np.transpose(train2))
theta2 = np.matmul(theta2, trainY)
theta3 = np.matmul(np.linalg.inv(np.matmul(np.transpose(train3), train3)), np.transpose(train3))
theta3 = np.matmul(theta3, trainY)


# use test dataset to evaluate the performance of both model, using MSE
test_mse2 = mean_squared_error(np.matmul(test2, theta2), testY)
test_mse3 = mean_squared_error(np.matmul(test3, theta3), testY)
answers['Q4'] = [test_mse2, test_mse3]
assertFloatList(answers['Q4'], 2)
print(answers)


