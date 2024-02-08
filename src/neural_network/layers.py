import numpy as np

class Layer:
	def __init__(self):
		pass
	
	def forward(self, input_data):
		raise NotImplementedError
	
	def backward(self, grad_output):
		raise NotImplementedError

class Dense(Layer):
	def __init__(self, input_dim, output_dim, learning_rate=0.01, activation=None):
		super().__init__()
		self.weights = np.random.randn(input_dim, output_dim) * 0.01
		self.biases = np.zeros(output_dim)
		self.learning_rate = learning_rate
		self.activation = activation
		self.input_data = None

	def forward(self, input_data):
		self.input_data = input_data
		return np.dot(input_data, self.weights) + self.biases
	
	def backward(self, grad_output):
		grad_weights = np.dot(self.input_data.T, grad_output)
		grad_biases = np.sum(grad_output, axis=0)
		grad_input = np.dot(grad_output, self.weights.T)
		
		self.weights -= self.learning_rate * grad_weights
		self.biases -= self.learning_rate * grad_biases
		
		return grad_input

class Activation(Layer):
	def __init__(self, forward_func, backward_func):
		super().__init__()
		self.forward_func = forward_func
		self.backward_func = backward_func
		self.input_data = None
	
	def forward(self, input_data):
		self.input_data = input_data
		return self.forward_func(input_data)
	
	def backward(self, grad_output):
		return self.backward_func(self.input_data) * grad_output

class Dropout(Layer):
	def __init__(self, rate):
		super().__init__()
		self.rate = rate
		self.mask = None

	def forward(self, input_data):
		self.mask = np.random.binomial(1, 1 - self.rate, size=input_data.shape) / (1 - self.rate)
		return input_data * self.mask
	
	def backward(self, grad_output):
		return grad_output * self.mask
