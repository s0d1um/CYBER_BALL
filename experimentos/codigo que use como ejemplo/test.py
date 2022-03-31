 # Module: f2.py # Example 1: functions to store and retrieve global variables 
 gMyVar = 0 
 def print_world():
 print "World!" def get_gMyVar():
 return gMyVar # no need for global statement
 def inc_gMyVar():
 global gMyVar gMyVar += 1 # Example 2: class methods to store and retrieve properties 
 class useMyVars(object): 
 	def __init__(self, myVar):
 		self.myVar = myVar
    def getMyVar(self): 
    	return self.myVar def setMyVar(self, myVar): self.myVar = myVar def print_helloWorld(self): print "Hello, World!" 