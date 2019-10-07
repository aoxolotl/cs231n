from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)
    num_classes = W.shape[1]

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_training = X.shape[0]
    for i in range(num_training):
        scores = X[i].dot(W)
        # normalization trick
        scores -= scores.max()
        probs = np.exp(scores)
        probs /= np.sum(probs)
        loss += -np.log(probs[y[i]])
        for j in range(num_classes):
            if j == y[i]:
                dW[:, j] += (probs[j] - 1) * X[i]
            else:
                dW[:, j] += probs[j] * X[i]

    loss /= num_training
    dW /= num_training
    
    loss += reg * np.sum(W*W)
    dW += 2 * reg * W
    
     # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)
    num_train = X.shape[0]

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    scores = X.dot(W)
    scores -= scores.max()
    #breakpoint()
    probs = np.exp(scores)
    probs /= np.sum(probs, axis = 1).reshape(num_train, 1)
    loss = -np.sum(np.log(probs[np.arange(num_train), y]))
    loss /= num_train
    
    jac = probs
    jac[np.arange(num_train), y] -= 1
    dW = X.T.dot(jac)
    dW /= num_train
    
    loss += reg * np.sum(W * W)
    dW += 2 * reg * W
    

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
