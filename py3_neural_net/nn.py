#'''This is a test neural net for predicting trends in fake data'''
# I am following tutorials from the "Neural Networks Demistified" playlist
#  by Welsh Labs
import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork(object):
    #'''
    #neural network class to train on basic data
    #net has one hidden layer.
    #'''
    def __init__(self, in_nodes=2, out_nodes=1, hidden_size=3):
        # Hyperparameters
        self.inputLayerSize = in_nodes
        self.outputLayerSize = out_nodes
        self.hiddenLayerSize = hidden_size

        # Initial Weights:
        self.w1 = np.random.randn(self.inputLayerSize, 
                        self.hiddenLayerSize)
        self.w2 = np.random.randn(self.hiddenLayerSize,
                        self.outputLayerSize)

    def forward(self, x):
        #'''Propegate inputs through the network'''
        self.z2 = np.dot(x, self.w1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.w2)
        yHat = self.sigmoid(self.z3)
        return yHat

    def sigmoid(self, z):
        #'''basic sigmoid activation function'''
        return 1/(1+np.exp(-z))

    def relu(self, z):
        #'''basic rectifier'''
        return max(0, z)

    def sigmoidPrime(self, z):
    #Derivitive of sigmoid function
        return np.exp(-z)/((1+np.exp(-z))**2)

    def costFunction(self, x, y):
        #compute cost for given x and y, with weights in the class
        self.yHat = self.forward(x)
        j = .5*sum((y-self.yHat)**2)
        return j

    def costFunctionPrime(self,x, y):
        #compute derivitive with respect to W1 and W2
        self.yHat = self.forward(x)

        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)
        
        delta2 = np.dot(delta3, self.w2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(x.T, delta2)

        return dJdW1, dJdW2

    def getParams(self):
        #get W1 and W2 rolled into a vec
        params = np.concatenate((self.w1.ravel(), self.w2.ravel()))
        return params
    
    def setParams(self, params):
        #set W1 and W2 using a param vec
        w1_start = 0
        w1_end = self.hiddenLayerSize * self.inputLayerSize
        self.w1 = np.reshape(params[w1_start:w1_end],
                        (self.inputLayerSize, self.hiddenLayerSize))
        w2_end = w1_end + self.hiddenLayerSize * self.outputLayerSize
        self.w2 = np.reshape(params[w1_end:w2_end],
                        (self.hiddenLayerSize, self.outputLayerSize))

    def computeGradients(self, x, y):
        dJdW1, dJdW2 = self.costFunctionPrime(x,y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))




# Part 3

x = np.array([[3,5],[5,1],[10,2]])

y = np.array([[.75], [.82], [.93]])

nn = NeuralNetwork()

yHat = nn.forward(x)

print("initial estimates")
print(yHat)
print("actual data")
print(y)

# Part 4

#show sigmoidPrime is the derivitive of sigmoid:

#testValues = np.arange(-5, 5, .01) #type is numpy.ndarray
#plt.plot(testValues, nn.sigmoid(testValues), linewidth=2)
#plt.plot(testValues, nn.sigmoidPrime(testValues), linewidth=2)
#plt.grid(1)
#plt.legend(['sigmoid', 'sigmoidPrime'])
#plt.show()

# Gradient descent!!

nn = NeuralNetwork()
cost1 = nn.costFunction(x,y)
dJdW1, dJdW2 = nn.costFunctionPrime(x,y)
print("\n\ndJdW1\n", dJdW1)
print("dJdW2\n", dJdW2)

scalar = 3
print("add scalar * the gradient to each weight")
nn.w1 = nn.w1 + scalar*dJdW1
nn.w2 = nn.w2 + scalar*dJdW2

cost2 = nn.costFunction(x,y)

print('"cost" or error increases')
print (cost1, cost2)

scalar = 3
dJdW1, dJdW2 = nn.costFunctionPrime(x,y)
print("subtract scalar * the gradient to each weight")
nn.w1 = nn.w1 - scalar*dJdW1
nn.w2 = nn.w2 - scalar*dJdW2
cost3 = nn.costFunction(x,y)

print('"cost" or error decreases')
print (cost2, cost3)
print("^^ This is the basis for gradient descent!!")


# part 5

#numeric gradient checking
#this is a numeric process to check the derivitive of the cost function

def f(x):
    return x**2
# the derivitive of x**2 is 2x
epsilon = 1e-4
x = 1.5


print("\n\nderivitive using definition: \nlim as deltaX->0 of (f(x + deltaX) - f(x))/deltaX")
numericGradient = (f(x+epsilon)-f(x-epsilon))/(2*epsilon)
print("\nnumericGradient of x**2:", numericGradient, "\n2*x = ", 2*x)
print("^^ They are similar, so the derivitive of x**2 has been \nnumerically confirmed to be 2x.\n\n")


def computeNumericalGradient(n, x, y):
    paramsInitial = n.getParams()
    numgrad = np.zeros(paramsInitial.shape)
    perturb = np.zeros(paramsInitial.shape)
    e = 1e-4

    for p in range(len(paramsInitial)):
        perturb[p] = e
        n.setParams(paramsInitial + perturb)
        loss2 = n.costFunction(x,y)

        n.setParams(paramsInitial - perturb)
        loss1 = n.costFunction(x,y)

        #compute the numeerical gradient
        numgrad[p] = (loss2 - loss1) / (2*e)

        #reset the value to zero
        perturb[p] = 0

    #reset params
    n.setParams(paramsInitial)

    return numgrad
    
x = np.array([[3,5],[5,1],[10,2]])

y = np.array([[.75], [.82], [.93]])

nn = NeuralNetwork()
numgrad = computeNumericalGradient(nn, x, y)
grad = nn.computeGradients(x,y)

print("If these look similar, our gradient calculation is correct.")
print(numgrad)
print(grad)

print("\nAnd this is a way to measure the difference more directly:")
print(np.linalg.norm(grad-numgrad)/np.linalg.norm(grad+numgrad))
print("^ If this is on the order of 10^-8 or less, we are correct.\n\n")
