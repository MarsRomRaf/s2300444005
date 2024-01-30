#import libraries
import numpy as np

#function definition for distance 
def calculate_braking_distance(initial_velocity, friction, gravity, time):
    velocity = initial_velocity - friction * gravity * time
    
    #initializes an array of zeros to the same shape of the velocity
    #braking_distance = np.like(velocity)
    #calculates de braking distance and then returns the output to the main code
    #for i in range(1, len(time)):
    #    braking_distance[i] = braking_distance[i - 1] + velocity[i] * (time[i] - time[i - 1])
    
    #cumulative sum of the elements in the velocity array
    #calculates braking distance over time
    braking_distance = np.cumsum(velocity) * (time[1] - time[0])
    #returns the braking distance to the main code
    return braking_distance
