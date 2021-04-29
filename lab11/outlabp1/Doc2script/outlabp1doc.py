#from math import exp
#from random import seed
#from random import random

"""
.. module:: outlabp1doc
    :platform: Ubuntu
    :synopsis: module documentation for training neural network
 
.. moduleauthor:: Akhil Dadi
"""

def backward_propagate_error(network, expected):
	"""
	
	calculates delta for entire network
	
	:type network: network
	:param network: neural network object
	
	:type expected: float
	:param expected: actual value of given data
	
	"""
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

def update_weights(network, row, l_rate):
	"""
	
	Updates weights of layers in network
	
	:type network: network
	:param network: neural network object
	
	:type row: float
	:param row: input for entire network
	
	:type l_rate: float
	:param l_rate: learning rate of network
	
	
	"""
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']

def train_network(network, train, l_rate, n_epoch, n_outputs):
	"""
	
	Train a network for a fixed number of epochs
	
	:type network: network
	:param network: neural network object
	
	:type train: float
	:param train: input for entire network to train
	
	:type l_rate: float
	:param l_rate: learning rate of network
	
	:type n_epoch: integer
	:param n_epoch: no of epochs
	
	:type n_outputs: intger
	:param n_outputs: number of output nodes	
	
	"""
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[row[-1]] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))


if __name__ == "__main__":
	"""
	Test backpropagation algorithm
	"""
	seed(1)
	dataset = [[2.7810836,2.550537003,0],
		[1.465489372,2.362125076,0],
		[3.396561688,4.400293529,0],
		[1.38807019,1.850220317,0],
		[3.06407232,3.005305973,0],
		[7.627531214,2.759262235,1],
		[5.332441248,2.088626775,1],
		[6.922596716,1.77106367,1],
		[8.675418651,-0.242068655,1],
		[7.673756466,3.508563011,1]]
	n_inputs = len(dataset[0]) - 1
	n_outputs = len(set([row[-1] for row in dataset]))
	network = initialize_network(n_inputs, 2, n_outputs)
	train_network(network, dataset, 0.5, 20, n_outputs)
	for layer in network:
		print(layer)
