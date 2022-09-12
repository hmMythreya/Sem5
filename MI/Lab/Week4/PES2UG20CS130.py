from re import subn
import numpy as np


class KNN:
    """
    K Nearest Neighbours model
    Args:
        k_neigh: Number of neighbours to take for prediction
        weighted: Boolean flag to indicate if the nieghbours contribution
                  is weighted as an inverse of the distance measure
        p: Parameter of Minkowski distance
    """

    def __init__(self, k_neigh, weighted=False, p=2):

        self.weighted = weighted
        self.k_neigh = k_neigh
        self.p = p

    def fit(self, data, target):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix( M data points with D attributes each)(float)
            target: Vector of length M (Target class for all the data points as int)
        Returns:
            The object itself
        """

        self.data = data
        self.target = target.astype(np.int64)

        return self

    def find_distance(self, x):
        """
        Find the Minkowski distance to all the points in the train dataset x
        Args:
            x: N x D Matrix (N inputs with D attributes each)(float)
        Returns:
            Distance between each input to every data point in the train dataset
            (N x M) Matrix (N Number of inputs, M number of samples in the train dataset)(float)
        """
        # self.data = X 
        # x = 2x2
        sum_ = []
        for i in range(len(x)):
            su_li = []
            for j in range(len(self.data)):
                su = 0
                for k in range(len(x[i])):
                    su += (x[i][k] - self.data[j][k])**self.p
                su = su**(1/self.p)
                su_li.append(su)
            sum_.append(su_li)
        for i in sum_:
            for j in range(len(i)):
                if i[j] < 0:
                    i[j] = -i[j]
        return sum_

    def k_neighbours(self, x):
        """
        Find K nearest neighbours of each point in train dataset x
        Note that the point itself is not to be included in the set of k Nearest Neighbours
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            k nearest neighbours as a list of (neigh_dists, idx_of_neigh)
            neigh_dists -> N x k Matrix(float) - Dist of all input points to its k closest neighbours.
            idx_of_neigh -> N x k Matrix(int) - The (row index in the dataset) of the k closest neighbours of each input

            Note that each row of both neigh_dists and idx_of_neigh must be SORTED in increasing order of distance
        """
        """
        Solution:
            di_ = array of all the distances.
            sort di_
            take the first k elements of di_
            if k is > di_.len(), return di_
            else return di_[:k]

            along with that we need to return the indexes 
        """
        di_ = self.find_distance(x)
        sorted_di = []
        for i in di_:
            sorted_di.append(i.copy())
        re_di = []
        for i in range(len(sorted_di)):
            sorted_di[i].sort()
            re_di.append(sorted_di[i][:self.k_neigh])

        
        indx_ = []
        #print(di_)
        for i in range(len(re_di)):
            li = []
            for j in range(self.k_neigh):
                #print(re_di[i][j])
                li.append(di_[i].index(re_di[i][j]))
            indx_.append(li)
        print(re_di,indx_)
        return [re_di,indx_]

    def predict(self, x):
        """
        Predict the target value of the inputs.
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            pred: Vector of length N (Predicted target value for each input)(int)
        """
        # TODO
        pass

    def evaluate(self, x, y):
        """
        Evaluate Model on test data using 
            classification: accuracy metric
        Args:
            x: Test data (N x D) matrix(float)
            y: True target of test data(int)
        Returns:
            accuracy : (float.)
        """
        # TODO
        pass
