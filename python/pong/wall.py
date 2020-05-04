#!/usr/bin/python3.7

import random

class Wall():
    """A class used to represent object for collision detection."""
    def __init__(self, vector, rectangle, color):
        """Initialize class instance."""
        self.vector = vector
        self.rectangle = rectangle
        self.color = color

        self.origin = self.rectangle
        
    def reset_position(self):
        """Restores original position."""
        self.rectangle = self.origin


class Player(Wall):
    """This class implements game object managed by the player."""
    def __init__(self, vector, rectangle, color):
        super().__init__(vector, rectangle, color)
        self._DX = 10

    def move_left(self):
        """Moves object to the left."""
        self.rectangle = self.rectangle.move(-self._DX, 0)

    def move_right(self):
        """Moves object to the right."""
        self.rectangle = self.rectangle.move(self._DX, 0)

class Ball(Wall):
    """This class implements ball object that bounce out the walls."""
    def __init__(self, vector, rectangle, color):
        """Initialize class instance."""
        super().__init__(vector, rectangle, color)
        self.vec_len = vector.length

    def update(self):
        """Implements move procedure."""
        dx, dy = self.vector.projections()
        self.rectangle = self.rectangle.move(dx, -dy)

    def bounce(self, vector):
        """Calculates bounce angle."""
        self.vector.angle = 2 * vector.angle + 180 - self.vector.angle

    def randomize_angle(self):
        """Provides angle randimization."""
        choise = random.choice([0, 1, 2, 3])
        
        if choise == 0:
            self.vector.angle = random.randint(30, 30 + 50)

        elif choise == 1:
            self.vector.angle = random.randint(100, 100 + 50)

        elif choise == 2:
            self.vector.angle = random.randint(210, 210 + 50)

        else:
            self.vector.angle = random.randint(280, 280 + 50)

    def start(self) -> None:
        """Restoring ball move speed."""
        self.vector.length = self.vec_len
    
    def stop(self) -> None:
        """Stop ball moving by setting speed to 0."""
        self.vector.length = 0
