# Class declaration
class Student:
    """
    A class that represents a student with id, firstname and lastname.
    Attributes:
    - id: The student 's id
    - firstname: The student 's firstname
    - lastname: The student 's lastname
    """
    def __init__(self, id, firstname, lastname):
        """
        Initialize a new instance of the Student class.
        Args:
        - id: The student 's id
        - firstname: The student 's firstname
        - lastname: The student 's lastname
        """
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname

    @property
    def id(self):
        """
        id getter:
        Gets the id of the instance of the Student class
        """
        return self.__id
    
    @id.setter
    def id(self, id):
        """
        id setter:
        Sets the id of the instance of the Student class
        """
        self.__id = id

    @property
    def firstname(self):
        """
        firstname getter:
        Gets the firstname of the instance of the Student class
        """
        return self.__firstname
    
    @firstname.setter
    def firstname(self, firstname):
        """
        firstname setter:
        Sets the firstname of the instance of the Student class
        """
        self.__firstname = firstname
    
    @property
    def lastname(self):
        """
        lastname getter:
        Gets the lastname of the instance of the Student class
        """
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname):
        """
        lastname setter:
        Sets the lastname of the instance of the Student class
        """
        self.__lastname = lastname