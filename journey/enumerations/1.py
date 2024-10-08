"""ENUMERATIONS FOR JOURNEY APP"""

import enum


class Color(enum.Enum):
    """
    ENUM for colors
    """

    RED = 1
    GREEN = 2
    BLUE = 3


class Status(enum.Enum):
    """
    ENUM for status
    """

    PENDING = 1
    RUNNING = 2
    COMPLETED = 3


class UnitVector(enum.Enum):
    """
    ENUM FOR UNIT VECTORS
    """

    V1D = (1,)
    V2D = (1, 1)
    V3D = (1, 1, 1)


print(Status.PENDING.name)
print(Status.PENDING.value)
