# -*- coding: utf-8 -*-

import random
import collections
import math
import time
from util import *

_X_ = None

############################################################
# Sentiment Classification
############################################################

# Problem B: extractWordFeatures

def extractWordFeatures(x):
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE
    phi = {}                    # or "phi = collections.defaultdict(int)"
    textlist=x.split()
    print(textlist)
    for i in textlist:
        if i in phi.keys():
            phi[i]+=1
        else :
            phi[i]=1
    # END_YOUR_CODE
    return phi

# Problem C: learnPredictor

def learnPredictor(trainExamples, testExamples, featureExtractor, numIters, eta):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, the step size |eta|, return the weight vector (sparse
    feature vector) learned, and error values lists for train and test datasets

    You should implement stochastic gradient descent.

    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and testExamples
    to see how you're doing as you learn after each iteration.
    '''
    # BEGIN_YOUR_CODE
    weights = {}
    trainErrorList = []
    testErrorList = []

    def predictor(x):
        phi = featureExtractor(x)
        if dotProduct(phi, weights) >= 0:
            y = 1
        else:
            y = -1
        return y

    for t in range(numIters):
        for trainExample in trainExamples:
            x, y = trainExample
            phi = featureExtractor(x)

            # calculate Loss value
            loss = max(0,1-predictor(x))          # use 'max' and 'dotProduct'

            # update the weight vector
            if loss > 0:
                increment(weights, weights, phi)  # 'increment' is defined in util.py

        train_error = evaluatePredictor(trainExamples, predictor)
        test_error = evaluatePredictor(testExamples, predictor)
        print ("%d-th iteration: train error = %.2f, test error = %.2f"% \
              (t, train_error, test_error))
        
        trainErrorList.append(train_error)
        testErrorList.append(test_error)

    # END_YOUR_CODE

    return weights, trainErrorList, testErrorList

# Problem F: extractBigramFeatures Problem
def extractBigramFeatures(x):
    """
    Extract unigram(word) and bigram features for a string x.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {('am', 'what'): 1, 'what': 1, ('I', 'am'): 2, 'I': 2, ('what', 'I'): 1, 'am': 2, ('<s>', 'I'): 1, ('am', '</s>'): 1}
    """
    input_list=x.split()
    # BEGIN_YOUR_CODE
    phi={}
    for i in range(len(input_list) - 1):
        k1,k2=input_list[i],input_list[i+1]
        tk=(k1,k2)
        if tk in phi.keys():
            phi[tk]+=1
        else :
            phi[tk]=1
    # END_YOUR_CODE
    return phi

############################################################
# k-means Clustering
############################################################

# Problem K: kmeans

def kmeans(examples, K, maxIters):
    '''
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of iterations to run for (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments, (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''
    # BEGIN_YOUR_CODE
    centers = random.sample(examples, K)
    assignments = [0] * len(examples)

    def get_l2_loss(center_id, example):
        center = centers[center_id]
        features = set(center.keys() + example.keys())
        return sum((center.get(feature,0) - example.get(feature,0))**2 for feature in features)  # use 'dict.get'

    for iter_cnt in range(maxIters):
        prev_assignments = assignments
        assignments = [0] * len(examples)

        # update assignments
        for example_id, example in enumerate(examples):
            assignments[example_id] = min((center_id for center_id in range(len(centers))),
                                          key=lambda x: get_l2_loss(x,example))  # use 'get_l2_loss'
        # early stopping
        if prev_assignments==assignments:
            print('early stopping k-means')
            break

        # update centers
        cluster_sizes = [0] * K
        cluster_sums = [{} for _ in range(K)]
        for example_id, example in enumerate(examples):
            cluster_id = assignments[example_id]    # use assignments
            cluster_sizes[cluster_id] += 1
            cluster_sum = cluster_sums[cluster_id]
            increment(cluster_sum, 1., example)

        centers = [{} for _ in range(K)]
        for cluster_id, center in enumerate(centers):
            cluster_sum = cluster_sums[cluster_id]
            cluster_size = cluster_sizes[cluster_id]
            if cluster_size > 0:
                for word in cluster_sum:
                    center[word] = cluster_sum[word]/cluster_size  # use 'cluster_sum'

    else:
        print('max iteration')

    loss = 0
    for example_id, example in enumerate(examples):
        loss += get_l2_loss(assignments[example_id], example)

    # END_YOUR_CODE

    return centers, assignments, loss


# Problem M: kmeans_optimized

def kmeans_optimized(examples, K, maxIters):
    '''
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of iterations to run for (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments, (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''
    # BEGIN_YOUR_CODE
    raise NotImplementedError
    # END_YOUR_CODE
    return centers, assignments, loss

def main():
    print(extractWordFeatures("ab cd ca d d a"))
    print(extractBigramFeatures("a b a b d c d c b db cb db cb"))
    

main()