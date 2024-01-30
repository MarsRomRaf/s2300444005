#import libraries
import argparse
import matplotlib.pyplot as plt
import numpy as np

#import functions
from velocity import calculate_velocity
from braking_distance import calculate_braking_distance

#main function
def main(args):
    
    #define friction coefficients
    friction_coefficients = {
        "concrete": {"dry": 0.65, "wet": 0.4},
        "ice": {"dry": 0.2, "wet": 0.1},
        "water": {"dry": 0.1},
        "sand": {"dry": 0.3},
        "gravel": {"dry": 0.35}
    }

    #Get the friction coefficient dependending on the provided suface and condition
    #the default is 0.3, if it can't be found the chosen parameters
    friction = friction_coefficients.get(args.surface_type, {}).get(args.condition, 0.3)
    gravity = 9.81

    #Time calculation
    time_to_stop = args.initial_velocity / (friction * gravity)
    #np.linspace return spaced number over a specified interval, which is 0 to 500
    time = np.linspace(0, time_to_stop, num=500)

    #Calculation of velocity and braking distance by sending the provided data to the classes created
    velocity = calculate_velocity(args.initial_velocity, friction, gravity, time)
    braking_distance = calculate_braking_distance(args.initial_velocity, friction, gravity, time)
    
    #Calculation of rule of thumb with the initial velocity
    initialvelocity=args.initial_velocity
    snormal=(initialvelocity/10)**2
    sreaction=(initialvelocity/10)*3
    sstop=snormal+sreaction
    #Prints the braking distance done with physics and rule of thumb
    print(f"The braking distance at the end is {braking_distance[-1]} meters.")
    print(f"The braking distance at the end with Rule of Thumb is {sstop} meters.")

    #velocity plot configurations
    plt.figure(figsize=(20, 10))
    plt.plot(time, velocity)
    plt.title('Velocity vs Time')
    plt.xlabel('Time [s]')
    plt.ylabel('Velocity [m/s]')
    plt.grid(True)
    plt.savefig('velocity_vs_time.pdf')

    #distance plot configurations
    plt.figure(figsize=(20, 10))
    plt.plot(time, braking_distance)
    plt.title('Braking Distance vs Time')
    plt.xlabel('Time [s]')
    plt.ylabel('Braking Distance [m]')
    plt.grid(True)
    plt.savefig('braking_distance_vs_time.pdf')

#if its running, it sets up an arg parser for the command lines arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Braking simulation.')
    
    #command lines arguments
    parser.add_argument('--mass', type=float, required=True, help='Mass of the vehicle in kg')
    parser.add_argument('--surface_type', type=str, required=True, help='Type of the surface (concrete, ice, water, sand, gravel)')
    parser.add_argument('--condition', type=str, required=True, help='Condition of the surface (dry, wet)')
    parser.add_argument('--inclination', type=float, required=True, help='Inclination of the surface in degrees')
    parser.add_argument('--initial_velocity', type=float, required=True, help='Initial velocity of the vehicle in m/s')

    #calls the main for processing
    args = parser.parse_args()
    main(args)
