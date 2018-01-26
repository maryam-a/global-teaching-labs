# Adapted from https://fiftyexamples.readthedocs.io/en/latest/gravity.html 

# Import Python Libraries
import math
from turtle import *

# Constants
# Gravitational Constant: m**3 kg**-1 s**-2
G = 6.67428e-11

# Assumed scale: 100 pixels = 1AU = distance between Earth and Sun
AU = (149.6e6 * 1000)     # 149.6 million km, in meters
SCALE = 200 / AU

TIMESTEP = 24 * 3600 # seconds

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
        """
        Turtle.__init__(self)
        self.name = name
        self.mass = mass
        self.vx = vx
        self.vy = vy
        self.px = px
        self.py = py
        self.pencolor(color)

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
        dx = other_body.px - self.px
        dy = other_body.py - self.py
        distance = math.sqrt(dx**2 + dy**2)

        # Report collision
        if distance == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other_body.name))

        # Calculate the magnitude of the gravitational force
        force = (G * self.mass * other_body.mass) / (distance**2)

        # Calculate the x- and y-components of the force
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * force
        fy = math.sin(theta) * force

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

                fx, fy = body.gravitational_force(other_body)
                total_fx += fx
                total_fy += fy

            # Update the velocities based on the forces
            body.vx += total_fx / body.mass * TIMESTEP
            body.vy += total_fy / body.mass * TIMESTEP

            # Update positions
            body.px += body.vx * TIMESTEP
            body.py += body.vy * TIMESTEP
            body.goto(body.px*SCALE, body.py*SCALE)
            body.dot(3)

def main():
    # Mass, mean orbital velocity, semimajor axis (planet/earth ratio)
    # https://nssdc.gsfc.nasa.gov/planetary/factsheet/
    sun = Body('Sun', 1.98892 * 10**30, 'yellow')
    earth = Body('Earth', 5.9742 * 10**24, 'blue', vy=29.783 * 1000, px=-1*AU)
    venus = Body('Venus', 4.8675 * 10**24, 'red', vy=-35.02*1000, px=0.723*AU)
    simulation([sun, earth, venus])

if __name__ == '__main__':
    main()
