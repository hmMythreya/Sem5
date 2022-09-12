from re import subn
import numpy as np

class KNN:
    def __init__(self, k_neigh, weighted=False, p=2):

        self.weighted = weighted
        self.k_neigh = k_neigh
        self.p = p

    def fit(self, data, target):
        self.data = data
        self.target = target.astype(np.int64)

        return self

    def find_distance(self, x):
        sum_ = []
        for i in range(len(x)):
            su_li = []
            for j in range(len(self.data)):
                su = 0
                for k in range(len(x[i])):
                    su += (abs(x[i][k] - self.data[j][k]))**self.p
                su = su**(1/self.p)
                su_li.append(su)
            sum_.append(su_li)
        for i in sum_:
            for j in range(len(i)):
                if i[j] < 0:
                    i[j] = -i[j]
        return sum_

    def k_neighbours(self, x):
        di_ = self.find_distance(x)
        sorted_di = []
        for i in di_:
            sorted_di.append(i.copy())
        re_di = []
        for i in range(len(sorted_di)):
            sorted_di[i].sort()
            if(self.k_neigh>len(sorted_di[i])):
                re_di.append(sorted_di[i])
            else:
                re_di.append(sorted_di[i][:self.k_neigh])

        indx_ = []
        for i in range(len(re_di)):
            li = []
            for j in range(self.k_neigh):
                #print(re_di[i][j])
                li.append(di_[i].index(re_di[i][j]))
            indx_.append(li)
        return [re_di,indx_]

    def predict(self, x):
        val,ind = self.k_neighbours(x)
        pred = []
        for i in ind:
            co_ = []
            for j in i:
                co_.append(self.target[j])
            pred.append(max(set(co_), key=co_.count))
        return pred

    def evaluate(self, x, y):
        pred = self.predict(x)
        correct = 0
        total = 0
        for i in pred:
            if i==y[total]:
                correct+=1
            total+=1
        return correct/total * 100