# Class declaration in Python
class Student:
    """
    A class that represents a person with firstname and lastname
    Attributes:
    - firstname (str) : the firstname of the person
    - lastname (str) : the lastname of the person
    """
    def __init__(self, firstname, lastname):
        """
        Initialize a new instance of the Person class.
        Args:
        - firstname (str) : the firstname of the person
        - lastname (str) : the lastname of the person
        """
        self.firstname = firstname
        self.lastname = lastname