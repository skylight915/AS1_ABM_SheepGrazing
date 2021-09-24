import random

#Create a Agent class to give agents attributes and behaviours
class Agent():
    
    def __init__ (self, environment, agents, y, x):
        #Randomise the starting location of an agent
        
            self.y=random.randint(0,99)
            """"Randomly assign the value of coordinate Y to an agent """
            
            self.x=random.randint(0,99)
            """"Randomly assign the value of coordinate X to an agent """
            
            self.environment = environment
            """ assign each agent to the environment"""
            
            self.agents = agents
            """ get the list of agents into each agent"""
            
            self.store = 0
               
            if (x == None):
                self._x = random.randint(0,100)
            else:
                self._x = x
            if (y == None):
                self._y = random.randint(0,100)
            else:
                self._y = y
            """"Make sure the code runs with missing y & x values"""
    
   
    def move(self):
         #Get agents randomly move and apply touros to avoid boundary effects
         
            if random.random() < 0.5:
                self.x = (self.x + 1) % 100
            else:
                self.x = (self.x - 1) % 100

            if random.random() < 0.5:
                self.y = (self.y + 1) % 100
            else:
                self.y = (self.y - 1) % 100
	
    
    def eat(self): 
        #Let agents interact/eat the environment
        
    		if self.environment[self.y][self.x] > 10:
                    self.environment[self.y][self.x] -= 10
                    self.store += 10
                    """while moving, each agents consumes 10 units of the environment 
                    should there is at least 10 units left therein"""
    
    
    def share_with_neighbours(self, neighbourhood):
        #Make agents scan each other & adjust themselves
        
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                """when the distance between two agents falls within the neighbourhood
                """
                print("sharing " + str(dist) + " " + str(ave)) 
    
  
    def distance_between(self, agent):
        #Calculate the distance between any two agents 
        
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
