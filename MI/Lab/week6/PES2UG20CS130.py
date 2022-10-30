from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import *
import pandas as pd
import numpy as np

class SVM:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        data = pd.read_csv(self.dataset_path)
        # X-> Contains the features
        self.X = data.iloc[:, 0:-1]
        # y-> Contains all the targets
        self.y = data.iloc[:, -1]

    def solve(self):
        return Pipeline([('scalar1',StandardScaler()), ('svm_classifier',SVC(kernel="rbf",gamma='scale',C=4))]).fit(self.X,self.y)
