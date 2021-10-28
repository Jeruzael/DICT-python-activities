class House:	
	__floorSize = 0
	__noOfFloors = 0
	__noOfDoors = 0

	def __init__(self, fs, nof, nod):
			self.__floorSize = fs
			self.__noOfFloors = nof
			self.__noOfDoors = nod

	def switchOn(self):
		print("Switch is On")
		self.lightOpen()
		self.ovenOpen()

	def lightOpen(self):
		print("Light is open")

	def ovenOpen(self):
		print("Over is open")

	def setNoOfFloors(self, nof):
		self.__noOfFloors = nof

	def setNoOfDoors(self, nod):
		self.__noOfDoors = nod
	

	def displayPpy(self):
		print(f"\nFloor Size: {self.__floorSize}\nNo. of floors: {self.__noOfFloors} \nNo. of Doors: {self.__noOfDoors}\n")
		
		