#!/usr/bin/env python
# coding: utf-8

# In[26]:


#!/usr/bin/env python
# coding: utf-8
# Name : Yusuf Mohammed
# FE520 Assignment 3
# In[ ]:


# Notice: do not change these function name 
class MovingAverage:

    def __init__(self, size):
        # A class instance is initialized with an empty list and the window size.
        # Defines an empty list to hold the stream of numbers.
        self.num_stream = []
        # Defines a variable to hold the provided window size.
        self.s = size
    
    def next(self, val):
        # Adds the provided value to the number stream list.
        self.num_stream.append(val)
        
        # Checks if number stream length is not larger than window.
        # If so, it will calculate sum of all elements of number stream.
        if len(self.num_stream) <= self.s:
            # Calculates average of relevant list of numbers.
            mov_avg = sum(self.num_stream) / len(self.num_stream)
        else :
            # If not, it will pick the last n elements of the number stream, where n is the window size.
            num_window = self.num_stream[-self.s:]
            # Calculates average of relevant list of numbers.
            mov_avg = sum(num_window) / self.s
        return round(mov_avg, 5)
    
class subway:

    def __init__(self):
        # Define empty dictionaries.
        self.travel = {} # Store customer id as key and start station name & trip start time as tuple value.
        self.average = {} # Store start station & end station names as tuple key and sum of travel time & number of trips as value tuple.
        
    def checkIn(self, id, stationName, t):
        # Assigns start station and start time as value tuple to travel dictionary with id as key.
        self.travel[id] = (stationName, t)
        
    def checkOut(self, id, stationName, t):
        # Retrieves start station name and start time with ID key from travel dictionary.
        startStation, startTime = self.travel.pop(id)
        
        # Calculate the current triptime.
        triptime = t - startTime
        
        # Initializes sum of travel time and number of trips.
        # These are local variables because they are specific to each pair of start and end station.
        sum_traveltime, num_of_trips = 0, 0
        
        # Checks if this pair of start and end stations has previous trip data and if so, assigns retrieved data.
        if (startStation, stationName) in self.average:
            sum_traveltime, num_of_trips = self.average[(startStation, stationName)]
        
        # Updates the sum of travel time and number of trips with the current checkout.
        self.average[(startStation, stationName)] = (sum_traveltime + triptime, num_of_trips + 1)
    
    def getAverageTime(self, startStation, endStation):
        # Retrieves and assigns the sum of travel time and number of trip for the specific start and end station travel.
        s, t = self.average[(startStation, endStation)]
        # Calculates the average travel time and returns a value with upto 3 decimals precision.
        return round(s / t, 3)

# Alternative function that uses more variables. 
# class subway:

#     def __init__(self):
#         self.start = {}
#         self.stop = {}
#         self.travel = {}
#         self.average = {}
#         self.trip_list = {}
        
        
#     def checkIn(self, id, stationName, t):
#         self.start[id] = [stationName, t]
#         self.travel[stationName] = {}
#         if id in self.trip_list.keys() :
#             pass
#         else :
#             self.trip_list[id] = []
       
    
#     def checkOut(self, id, stationName, t):
#         self.stop[id] = [stationName, t]
#         start_time = self.start[id][1]
#         trip_time = t - start_time
#         self.trip_list[id].append(trip_time)
#         #print(self.trip_list[id])
#         start_station =  self.start[id][0]
#         self.travel[start_station] = {stationName : self.trip_list[id]}

    
#     def getAverageTime(self, startStation, endStation):
#         #print(self.start)
#         #print(self.stop)
#         #print(self.travel)
#         #print(self.average)
#         #print(self.trip_list)
#         traveltime = self.travel[startStation][endStation]
#         return round(sum(traveltime) / len(traveltime), 3)

    

class Linear_regression:

    def __init__(self, x, y, m, c, epochs, L):
        # Assigns provided values to class variables.
        self.x = x
        self.y = y
        self.m = m
        self.c = c
        self.epochs = epochs
        self.L = L
        
        
    def gradient_descent(self) :
        # Calculates the length of the input x list.
        n = len(self.x)
        
        # Performs number of loops as provided by variable epochs. 
        for z in range(self.epochs):
            # Defines predictive dependent variable ypred list, calculated from formula.
            ypred = []
            # Defines empty list Dm and Dc.
            Dm = []
            Dc = []
            # Loops for length of the x list, calculates predicted values for y.
            # Appends calculated values to Dm and Dc list.
            for i in range(n) :
                ypred.append([self.x[i][0]*self.m + self.c])
                Dm.append(self.x[i][0]*(ypred[i][0]-self.y[i]))
                Dc.append(ypred[i][0]-self.y[i])

            # Defines sum of element in Dm and Dc.
            sumDm = 0
            sumDc = 0
            # Loops and sums the values in Dm and Dc.
            for i in range(n) :
                sumDm += Dm[i]
                sumDc += Dc[i]

            # Calculates average value of elements of Dm and Dc.
            dm = sumDm / n
            dc = sumDc / n

            # Based on values of dm and dc, updates new values of m and c.
            self.m = self.m - self.L*dm
            self.c = self.c - self.L*dc

        return (self.m,self.c)
    
    
    def predict(self,x_new):
        # Calculates the length of the input x_new list.
        n = len(x_new)
        
        # Defines a new empty list that will store the output values.
        ypred = []
        
        # Loops through the elements of input x.
        # Predicts the corresponding values for y using the linear formula and the updated values of m and c.
        # Appends predicted y values to ypred list.
        for i in range(n) :
            ypred.append(x_new[i]*self.m + self.c)
        
        # Returns the list of predicted values.
        return (ypred)
    
    
class LCG:

    def __init__(self, seed, multiplier, increment, modulus):
        # Creates an empty list X for sequence of integers starting with seed as first number.
        self.X = []
        # Creates an empty list seqlist for sequence of random numbers.
        self.seqlist = []
        # Assigns provided values to class variables.
        self.seed = seed
        self.X.append(seed)
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        
    def get_seed(self): 
        # Returns current seed value - first element of X list
        return self.seed
         
    def set_seed(self,new_seed): 
        # Assigns parameter to seed value
        self.seed = new_seed
        self.X[0] = self.seed
        return self.seed
    
    def initialize(self):
        return self.seed
    
    def gen(self):
        self.X.append((self.multiplier*self.X[-1]+self.increment)%self.modulus)
        self.seqlist.append(self.X[-1] / self.modulus)
        return self.seqlist[-1]
        
    def seq(self, num):
        le = len(self.X)
        # Loops and generates next "num" number of random numbers in the sequence
        for i in range(le,le + num) :
            self.gen()
        # Returns the sliced list of seqlist for the next "num" number of values
        return (self.seqlist[le - 1:le + num])
        # Returns the sliced list of seqlist for the first "num" number of values
        #return (self.seqlist[0:num])



if __name__ == "__main__":  

    x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    x_new = [0.9,0.8,0.40,0.7]

    
    # Test Question 1
    print("\nQ1")    
    windowsize = 3 
    moving_average = MovingAverage(windowsize)
    step1 = moving_average.next(1)  
    print("my answer: ", step1)    
    print("right answer: 1.0")    
    print("--------------")
    step2 = moving_average.next(10) 
    print("my answer: ", step2)    
    print("right answer: 5.5")    
    print("--------------")  
    step3 = moving_average.next(3) 
    print("my answer: ", step3)    
    print("right answer: 4.66667")    
    print("--------------") 
    step4 = moving_average.next(5) 
    print("my answer: ", step4)    
    print("right answer: 6.0")    
    print("--------------") 
    
    
    
    # Test Question 2
    print("\nQ2") 
    s = subway()
    s.checkIn(10,'Leyton',3)
    s.checkOut(10,'Paradise',8)
    print("my answer: ",s.getAverageTime('Leyton','Paradise'))
    print("right answer: 5.0")    
    print("--------------") 
    s.checkIn(10,'Leyton',10)
    s.checkOut(10,'Paradise',16)
    print("my answer: ",s.getAverageTime('Leyton','Paradise'))
    print("right answer: 5.5")    
    print("--------------") 
    s.checkIn(10,'Leyton',21)
    s.checkOut(10,'Paradise',30)
    print("my answer: ",s.getAverageTime('Leyton','Paradise'))
    print("right answer: 6.667")    
    print("--------------") 
    
    
    # Test Question 3
    print("\nQ3") 
    Linear_model = Linear_regression(x,y,0,0,500,0.001)
    print("I use m=0, c=0, epochs=500, L=0.001")
    print("my m and c: ",Linear_model.gradient_descent())
    print("right m and c:(35.97890301691016, 46.54235227399102)")    
    print("--------------") 
    print("my predict: ", Linear_model.predict(x_new))
    print(" right predict: [78.92336498921017, 75.32547468751915, 60.93391348075509, 71.72758438582812]")
    
    
    # Bonus Question 
    print("\nBonus") 
    print("set seed = 1, multiplier = 1103515245, increment = 12345, modulus = 2**32")
    lcg = LCG(1,1103515245,12345, 2**32 )
    print("my seed is: ", lcg.get_seed())
    print("right seed is: 1")
    print("the seed is setted with: ", lcg.set_seed(5))
    print("right seed is setted with 5")
    print("the LCG is initialized with seed: ",lcg.initialize())
    print("the LCG is initialized with seed 5")
    print("the next random number is: ", lcg.gen())
    print("right next random number is: 0.2846636981703341")
    print("the first ten sequence is: ", lcg.seq(10))
    print("the first ten sequence is: ", [0.6290451611857861, 0.16200014390051365, 0.4864134492818266, 0.655532845761627, 0.8961918593849987, 0.2762452410534024, 0.8611323081422597, 0.9970241007395089, 0.798466683132574, 0.46138259768486023])



# In[ ]:




