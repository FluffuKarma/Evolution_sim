import random
import math
import numpy
numpy.seterr(divide='ignore', invalid='ignore')

class newCreature():
	def __init__(self, spontaneous_pop, death, divide, mutate, number, X, Y, color):
		self.creatureKinds=[[spontaneous_pop, death, divide, mutate, 0]]
		self.creatures=[[random.randint(20, X-20),random.randint(20, Y-20), color, 0] for i in range(number)]
		self.BLACK = (  0,   0,   0)
		self.X=X
		self.Y=Y

	def addCreature(self, spontaneous_pop, death, divide, mutate, color):
		self.creatureKinds.append([spontaneous_pop, death, divide, mutate, creatures[-1][4]])

	def update(self):

		#TODO:
		#update over each creature kind for spontaneous pop
		#update over each creatures for each parameter


		#gets vector for random angle. Does mouvement of length 1

		for i in range(len(self.creatures)):
			vector=numpy.array([random.randint(-100,100), random.randint(-100,100)])
			vector=vector/(math.sqrt(vector[0]**2 + vector[1]**2))

			if self.creatures[i][0]+vector[0]+20 > self.X or (self.creatures[i][0]+vector[0])-20 < 0:
				vector[0]*=-1

			if self.creatures[i][1]+vector[1]+20 > self.Y or (self.creatures[i][1]+vector[1])-20 < 0:
				vector[1]*=-1

			self.creatures[i][0]+=vector[0]
			self.creatures[i][1]+=vector[1]

		return self.creatures
