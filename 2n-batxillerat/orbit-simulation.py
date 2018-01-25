# Adapted from https://fiftyexamples.readthedocs.io/en/latest/gravity.html 

# Import Python Libraries
import math
from turtle import *

# Constants
# Gravitational Constant (Unit: m**3 kg**-1 s**-2)
G = #TODO

# 1AU = distance between Earth and Sun (Unit: m)
AU = #TODO     
# Assume 100 pixels ~ 1AU
SCALE = 200 / AU

# Each step in the simulation corresponds to a day (Unit: s)
TIMESTEP = #TODO

class Body(Turtle):
    """
    Subclass of Turtle representing a gravitationally-acting body.
    """
    def __init__(self, name, mass, color, vx=0.0, vy=0.0, px=0.0, py=0.0):
        """
        Initializes an instance of the Body object
        Args:
            name (str): the name of the body
            mass (float): the mass of the body
            color (string OR tuple): the color of the pen to draw the motion of the body
            vx (float): the horizontal component of the mean orbital velocity of the body
            vy (float): the vertical component of the mean orbital velocity of the body
            px (float): the horizontal position of the body
            py (float): the vertical position of the body

        #TODO: 
        - Don't forget that the Body class is a subclass of the Turtle class. 
            Therefore, you need to initialize it.
        - Initialize the attributes of the Body class e.g. self.name = name
        """

        self.pencolor(color)
        raise NotImplementedError
        
    def gravitational_force(self, other_body):
        """
        Calculates the gravitational force between two bodies.
        Args:
            other_body (Body): the other satellite object
        Returns:
            The horizontal and vertical components of the gravitational force between two bodies.
        """
        # The body cannot be attracted to itself
        if self is other_body:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        # Calculate the distance between the two bodies
        dx = #TODO
        dy = #TODO
        distance = #TODO

        # Abort if the bodies collide
        if distance == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other_body.name))
        
        # Calculate the magnitude of the gravitational force
        force = #TODO

        # Calculate the x- and y- components of the force
        # Hint 1: Draw a diagram of the forces to determine how to calculate
        #           the angle between the horizational and vertical components
        # Hint 2: the math.atan2 function is useful
        theta = #TODO
        fx = #TODO
        fy = #TODO

        return fx, fy

def display_status(step, bodies):
    """
    Prints the position and velocity of the bodies at a certain step
    Args:
        step (int): the stage in the simulation
        bodies ([Body]): the bodies in the simulation
    """
    print('Step #{}'.format(step))
    for body in bodies:
        s = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(
            body.name, body.px/AU, body.py/AU, body.vx, body.vy)
        print(s)
    print()

def simulation(bodies):
    """
    Loops through the simulation. Updates the positions of the bodies.
    Args:
        bodies ([Body]): the list of bodies in the simulation
    """
    for body in bodies:
        body.penup()
        body.hideturtle()

    step = 1

    while True:
        display_status(step, bodies)
        step += 1

        for body in bodies:
            total_fx = total_fy = 0

            # Calculate the total forces on each body
            for other_body in bodies:
                # Ignore the body itself
                if body is other_body:
                    continue
                
                #Calculate the horizontal and vertical components of the force
                # between 'body' and 'other_body'
                fx, fy = #TODO
                total_fx += #TODO
                total_fy += #TODO

            # Update the velocities based on the forces
            body.vx += #TODO
            body.vy += #TODO

            # Update positions
            body.px += #TODO
            body.py += #TODO
            body.goto(body.px*SCALE, body.py*SCALE)
            body.dot(3)

def main():
    # Mass (mass), mean orbital velocity (vy), semimajor axis [planet/earth ratio] (px)
    # https://nssdc.gsfc.nasa.gov/planetary/factsheet/
    sun = Body('Sun', 1.98892 * 10**30, 'yellow')
    earth = Body('Earth', 5.9742 * 10**24, 'blue', vy=29.783*1000, px=-1*AU)
    venus = Body('Venus', 4.8675 * 10**24, 'red', vy=-35.02*1000, px=0.723*AU)
    simulation([sun, earth, venus])

if __name__ == '__main__':
    main()