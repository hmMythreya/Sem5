import numpy as np
class KMeansClustering:
    def __init__(self, n_clusters, n_init=10, max_iter=1000, delta=0.001):

        self.n_cluster = n_clusters
        self.n_init = n_init
        self.max_iter = max_iter
        self.delta = delta

    def init_centroids(self, data):
        idx = np.random.choice(
            data.shape[0], size=self.n_cluster, replace=False)
        self.centroids = np.copy(data[idx, :])

    def fit(self, data):
        if data.shape[0] < self.n_cluster:
            raise ValueError(
                'Number of clusters is grater than number of datapoints')

        best_centroids = None
        m_score = float('inf')

        for _ in range(self.n_init):
            self.init_centroids(data)

            for _ in range(self.max_iter):
                cluster_assign = self.e_step(data)
                old_centroid = np.copy(self.centroids)
                self.m_step(data, cluster_assign)

                if np.abs(old_centroid - self.centroids).sum() < self.delta:
                    break

            cur_score = self.evaluate(data)

            if cur_score < m_score:
                m_score = cur_score
                best_centroids = np.copy(self.centroids)

        self.centroids = best_centroids

        return self

    def e_step(self, data):
        distArr = []
        totdata = len(data)
        totcent = len(self.centroids)

        for i in range(totdata):
            for j in range(totcent):
                distArr.append(np.linalg.norm(self.centroids[j]-data[i]))

        re = []
        distance=np.reshape(distArr,(totdata,totcent))

        for i in range(totdata):
            re.append(np.argmin(distance[i]))  

        return re
    
    def m_step(self, data, cluster_assgn):
        r=len(self.centroids)
        c=len(self.centroids[0])

        cent=np.zeros(shape=(r,c))
        j=0

        for i in cluster_assgn:
            cent[i]=np.add(cent[i],data[j])
            j+=1

        cluster_assgn=np.array(cluster_assgn)

        for k in range(len(cent)):
            count=(cluster_assgn==k).sum()
            cent[k]=cent[k]*(1/count)  

        self.centroids=cent

    def evaluate(self, data):
        dist=[]
        totdata = len(data)
        totcent = len(self.centroids)
        for i in range(totdata):
            for j in range(totcent):
                dist.append((self.centroids[j]-data[i])*(self.centroids[j]-data[i]))
        dist = np.sum(dist, axis=1)
        err = 0
        for i in dist:
            err += i
        return err