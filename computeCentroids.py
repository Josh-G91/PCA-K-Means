import numpy as np


def compute_centroids(X, idx, K):
    # Useful values
    (m, n) = X.shape

    # You need to return the following variable correctly.
    centroids = []

    # ===================== Your Code Here =====================
    # Instructions: Go over every centroid and compute mean of all points that
    #               belong to it. Concretely, the row vector centroids[i]
    #               should contain the mean of the data points assigned to
    #               centroid i.
    #
    # ==========================================================
    for k in range(K):
       centroids.append((1/X[np.where(idx==k)].shape[0]*np.sum(X[(np.where(idx==k))],axis=0)))
    return np.array(centroids)
