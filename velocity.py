#import libraries
import numpy as np

#function definition for velocity
def calculate_velocity(initial_velocity, friction, gravity, time):
    #calculates de velocity
    velocity = initial_velocity - friction * gravity * time
    #returns to the main code the calculated velocity
    return velocity
   