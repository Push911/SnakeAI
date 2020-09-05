from ReinforcementLearning import Environment
from keras import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from collections import deque
import numpy as np
import random


class QLearning:
	def __init__(self):
		self.env = Environment.Environment()
		self.actionSpace = self.env.actionSpace
		self.stateSpace = self.env.stateSpace
		self.epsilon = 1
		self.gamma = 0.95
		self.batchSize = 500
		self.epsilonMin = 0.01
		self.epsilonDecay = 0.99
		self.learningRate = 0.0005
		self.episodes = 50
		self.layersSize = [128, 128, 128]
		self.rewards = 0
		self.memory = deque(maxlen=2500)
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

	def save(self, state, action, reward, nextState, done):
		self.memory.append((state, action, reward, nextState, done))

	def act(self, state):
		if np.random.rand() <= self.epsilon:
			return random.randrange(self.actionSpace)
		actValues = self.model.predict(state)
		return np.argmax(actValues[0])

	def replay(self):
		if len(self.memory) < self.batchSize:
			return

		batch = random.sample(self.memory, self.batchSize)
		states = np.array([i[0] for i in batch])
		actions = np.array([i[1] for i in batch])
		rewards = np.array([i[2] for i in batch])
		nextStates = np.array([i[3] for i in batch])
		dones = np.array([i[4] for i in batch])

		states = np.squeeze(states)
		nextStates = np.squeeze(nextStates)

		targets = rewards + self.gamma * (np.amax(self.model.predict_on_batch(nextStates), axis=1)) * (1 - dones)
		targetsFull = self.model.predict_on_batch(states)

		index = np.array([i for i in range(self.batchSize)])
		targetsFull[[index], [actions]] = targets

		self.model.fit(states, targetsFull, epochs=1, verbose=0)

		if self.epsilon > self.epsilonMin:
			self.epsilon *= self.epsilonDecay

	def trainModel(self):
		sumOfRewards = []

		for episode in range(self.episodes):
			state = self.env.reset()
			state = np.reshape(state, (1, self.env.stateSpace))
			score = 0
			steps = 10000
			for i in range(steps):
				action = self.act(state)
				previousState = state
				nextState, reward, done, _ = self.env.step(action)
				score += reward
				nextState = np.reshape(nextState, (1, self.env.stateSpace))
				state = nextState

				if self.batchSize > 1:
					self.replay()

				if done:
					print(f"Final state before death: {str(previousState)}")
					print(f"Episode: {episode + 1}/{self.episodes}. Score: {score}")
					break

			sumOfRewards.append(score)
		return sumOfRewards


if __name__ == "__main__":
	agent = QLearning()
	agent.trainModel()
