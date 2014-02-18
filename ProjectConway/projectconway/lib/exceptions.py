"""
This module contains a list of useful exceptions for the ProjectConway website
"""


class RunSlotTakenError(Exception):
    """
    This exception signifies that run slot is already populated
    """
    pass


class RunSlotInvalidError(Exception):
    """
    This exception signifies the run slot is invalid
    """
    pass