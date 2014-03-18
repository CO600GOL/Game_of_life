"""
This module contains some newly defined exceptions used to represent errors in the Project Conway web application.
"""


class RunSlotTakenError(Exception):
    """
    This exception signifies that a run slot has already been populated.
    """
    pass


class RunSlotInvalidError(Exception):
    """
    This exception signifies that a run slot is for some reason invalid.
    """
    pass