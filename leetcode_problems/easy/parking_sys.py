#constant time and space
class ParkingSystem():
	"""docstring for ParkingSystem"""
	def __init__(self, big, medium, small):
		#parking is a list of available parking for each
		#type of spot; 
		#index 0 -> number of big parking spots available, indx 1 ->med, ...
		self.parking = [big, medium, small]

	#carType can be big, medium, or small == 1, 2, or 3, respectively
	def addCar(self, carType):
		#let's make sure the input is in the correct range (1, 2, or 3)
		avaliablility = False
		if carType < 4 and carType > 0:
			if self.parking[carType - 1] > 0:	#check if a spot is open
				self.parking[carType - 1] -= 1	#take the spot
				availablility = True


		return availablility

