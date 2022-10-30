import numpy as np
from sklearn.tree import DecisionTreeClassifier

class AdaBoost:
    def __init__(self, n_stumps=20):
        self.n_stumps = n_stumps
        self.stumps = []

    def fit(self, X, y):
        self.alphas = []

        sample_weights = np.ones_like(y) / len(y)
        for _ in range(self.n_stumps):

            st = DecisionTreeClassifier(
                criterion='entropy', max_depth=1, max_leaf_nodes=2)
            st.fit(X, y, sample_weights)
            y_pred = st.predict(X)

            self.stumps.append(st)

            error = self.stump_error(y, y_pred, sample_weights=sample_weights)
            alpha = self.compute_alpha(error)
            self.alphas.append(alpha)
            sample_weights = self.update_weights(
                y, y_pred, sample_weights, alpha)

        return self

    def stump_error(self, y, y_pred, sample_weights):
        wrong = np.where(y_pred!=y,1,0)
        return np.sum(sample_weights*wrong)/np.sum(sample_weights)

    def compute_alpha(self, error):
        eps = 1e-9
        return (0.5)*np.log((1-error)/(error+eps))

    def update_weights(self, y, y_pred, sample_weights, alpha):
        error = self.stump_error(y, y_pred, sample_weights)
        if not error:
            return (sample_weights)* np.exp(alpha * (np.not_equal(y, y_pred)).astype(int))  
        for i in range(len(sample_weights)):
            if y[i] == y_pred[i]:
                sample_weights[i] = sample_weights[i]/(2*(1-error))
            else:
                sample_weights[i] = sample_weights[i]/(2*error)
        return sample_weights

    def predict(self, X):
        result = []
        ans = []
        for i in range(self.n_stumps):
            result.append(np.sign(self.stumps[i].predict(X)))
        for i in range(self.n_stumps):
            for j in range(len(result[0])):
                if not result[i][j]:
                    result[i][j] = -1
        for i in range(len(result[0])):
            s=0
            for j in range(self.n_stumps):
                s += self.alphas[j]*result[j][i]
            ans.append(np.sign(s))
        for i in range(len(ans)):
            if ans[i] == -1:
                ans[i] = 0
        return ans

    def evaluate(self, X, y):
        pred = self.predict(X)
        correct = (pred == y)
        accuracy = np.mean(correct) * 100  # accuracy calculation
        return accuracy