"""
File containing the phase class
"""


class Phase:
    """
        Base class for phase classes
    """
    phase_num = 0

    def __init__(self, initial):
        self.initial = initial
        Phase.phase_num += 1
        self.phase_num = Phase.phase_num
