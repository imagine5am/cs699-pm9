#from math import exp
#from random import seed
#from random import random

"""
.. module:: outlabp1doc
    :platform: Ubuntu
    :synopsis: module documentation for initializing neural network and activations
 
.. moduleauthor:: Akhil Dadi
"""

def initialize_network(n_inputs, n_hidden, n_outputs):
	"""
	
	Initializes weights in a neural network
	
	:type n_inputs: integer
	:param n_inputs: number of input nodes
	
	:type n_hidden: integer
	:param n_hidden: number of hidden layers
	
	:type n_outputs: integer
	:param n_outputs: number of output nodes
	
	:returns: network object with weights initialized
	
	
	"""
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network

def activate(weights, inputs):
	"""
	
	Calculates Z(W*X) of a layer in neural network
	
	:type weights: float
	:param weights: weight vector of given layer
	
	:type inputs: float
	:param inputs: input to current layer
	
	:returns: Z values of each layer(Z=w*x)
	
	"""
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation

def transfer(activation):
	"""
	
	Calculates activation(input to next layer) neural network
	
	:type activation: float
	:param activation: output of current layer
	
	:returns: activations of each layer
	
	"""
	return 1.0 / (1.0 + exp(-activation))

def forward_propagate(network, row):
	"""
	
	Does forward propagation to calculate activations of all layers
	
	:type network: network
	:param network: neural network object
	
	:type row: float
	:param row: input for entire network
	
	:returns: predicted y values after forward propogation	
	
	"""
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs

def transfer_derivative(output):
	"""
	
	returns derivative of activation function
	
	:type output: float
	:param output: output of current layer
	
	:returns: gradient of activation function
	
	"""
	return output * (1.0 - output)


