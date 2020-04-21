#!/usr/bin/python3.7

import math

class Vector:
    """A class used to represent object orientation in 2D space."""
    def __init__(self, angle, length = 0):
        """Initialize class instance."""
        self.set_angle(angle)
        self.set_length(length)

    def get_angle(self) -> int:
        """Return direction angle."""
        return self.__angle

    def set_angle(self, angle) -> None:
        """Assign new direction angle."""
        self.__angle = angle % 360

    def get_length(self) -> int:
        """Return vector's length."""
        return self.__length

    def set_length(self, length) -> None:
        """Assign new vector's length."""
        if length >= 0:
            self.__length = length
        else:
            exit('provided invalid length value {}'.format(length))

    def projections(self) -> tuple:
        """Return vector's projections on x and y axis."""
        dx = int(self.__length * math.cos(math.radians(self.__angle)))
        dy = int(self.__length * math.sin(math.radians(self.__angle)))

        return dx, dy

    def mirror_angle(self) -> None:
        """Set vector to opposite direction."""
        self.__angle = (self.__angle + 180) % 360

    def __str__(self) -> str:
        """Return information about vector properties."""
        return 'vector angle {}, length {}'.format(self.__angle, self.__length)

    angle = property(get_angle, set_angle)
    length = property(get_length, set_length)