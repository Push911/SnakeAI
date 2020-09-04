from ReinforcementLearning import Environment
from keras import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


class QLearning:
	def __init__(self):
		self.env = Environment()
		self.actionSpace = self.env.actionSpace
		self.stateSpace = self.env.stateSpace
		self.epsilon = 1
		self.gamma = 0.95
		self.batchSize = 500
		self.epsilonMin = 0.01
		self.epsilonDecay = 0.99
		self.learningRate = 0.001
		self.episodes = 50
		self.layersSize = [128, 128, 128]
		self.rewards = 0
		self.model = self.createModel()

	def createModel(self):
		model = Sequential()

		for i in range(len(self.layersSize)):
			if i == 0:
				model.add(Dense(self.layersSize[i], input_shape=(self.stateSpace,), activation="relu"))
			else:
				model.add(Dense(self.layersSize[i], activation="relu"))
				
			model.add(Dense(self.actionSpace, activation="softmax"))
			model.compile(loss="mse", optimizer=Adam(lr=self.learningRate))

		return model
