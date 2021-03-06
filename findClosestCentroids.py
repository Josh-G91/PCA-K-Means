import numpy as np


def find_closest_centroids(X, centroids):
    # Set K
    K = centroids.shape[0]

    m = X.shape[0]

    
    # You need to return the following variables correctly.
    idx = []

    for x in X:
        temp = []
        j = 0
        for c in centroids:
           temp.append((np.linalg.norm(x-c), j))
           j+=1
        idx.append(min(temp)[1])




    # ===================== Your Code Here =====================
    # Instructions : Go over every example, find its closest centroid, and store
    #                the index inside idx at the appropriate location.
    #                Concretely, idx[i] should contain the index of the centroid
    #                closest to example i. Hence, it should be a value in the
    #                range 0..k
    #
    
    


    # ==========================================================

    return np.asarray(idx)
