"""
Creator: Tyler Stanton

44-608, Fundamentals of Data Analytics
Project 2 - Task 5

The purpose of this code is to create a class based on movie review ratings

"""


from util_datafun_logger import setup_logger

class NumericMovieSeries:
    """
    A class (template) representing a numeric list of data with a name and units.

    Attributes:
        data (list): the data held by the object
        name (str): a descriptive name for the data
        units (str): the units associated with the data
    """

    def __init__(self, name, units, data):
        """
        Initialize the object when first created using the name, units, and data passed in through the constructor method.
        The two underscores before and after indicate this is a special method.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            data (list): the list of numeric data to be held by the object
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured

        """

        # initialize the object's attributes 
        # attribute is a special word for "data in an object"
        self.name = name
        self.units = units
        self.data = data

    # define methods that can be used on the object
    # method is a special word for "function in an object"
    # In Python, the first arugment of a method is always self - the object itself
    def count(self):
        """ 
        Get the count of elments in the data list.

        @return: the count of elements
        """
        return len(self.data)

    def mean(self):
        """
        Calculate the mean of the data list
        @return: float - the mean of the data
        """
        return sum(self.data) / len(self.data)

    def median(self):
        """
        Calculate the median of the data.
        @return: float -  the median of the data
        """
        sorted_data = sorted(self.data)
        n = len(self.data)
        if n % 2 == 0:
            return (sorted_data[n//2-1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]
        
    def sum(self):
        """ 
        Calculate the sum of the data.
        @return: the sum of the data
        """
        return sum(self.data)

    def variance(self):
        """
        Calculate the variance of the data.

        Returns:
            float: the variance of the data
        """
        n = len(self.data)
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / (n - 1)

    def standard_deviation(self):
        """
        Calculate the standard deviation of the data.

        Returns:
            float: the standard deviation of the data
        """
        return self.variance() ** 0.5

    def __str__(self):
        """
        Return a string representation of the instantiated object.
        The two underscores before and after indicate this is a special method.
        Every class needs a __str__ method that returns a string representation of the object.
        Be sure to use self.attribute_name so you use the object's attribute, not a local variable! 

        Returns:
            str: a string representation of the instantiated object
        """
        str = f"NumericMovieSeries with name={self.name}, units={self.units}, and {len(self.data)} data points: {self.data}"
        return str





if __name__ == "__main__":
    # If we're running this script (instead of using it in another class or script), 
    # Run some code to try our class

    # First, setup logging

    logger, logname = setup_logger(__file__)

    # Create an object by calling the constructor 
    # The constructor method is always the name of the class
    # pass in the information required by the __init__ method defined in the class

    name1 = "Movie Scores Module 1"
    units1 = "rating"
    data1 = [75, 90, 56, 84, 79, 67]

    object1 = NumericMovieSeries(name1, units1, data1)

  
    # Create another object

    name2 = "Movie Scores Module 2"
    units2 = "rating"
    data2 = [81, 43, 63, 72, 96, 32, 78, 60]

    object2 = NumericMovieSeries(name2, units2, data2)
    
    # Create another object 

    # use range() to create a list of values from 7 to 10
    # list() converts the range object to a list
    # range() is a generator - it creates a sequence of numbers without storing them in memory
    # The arguments in range are from (inclusive) and to (exclusive)
    data3 = list(range(70,80))    
    name3 = "Movie Scores Module 3"
    units3 = "rating"
    
    object3 = NumericMovieSeries(name3, units3, data3)

    # log the objects created
    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")
    logger.info(f"Created: {object3}")

    object_list = [object1, object2, object3]

    # Loop through our objects and get some statistics
    # Rather than using a built-in function and passing in our data
    # we call methods directly on our objects
    # Why? It's just another way to organize and reuse code. 
    # We encapusulate (wrap up) the attributes and associated methods into a resuable class. 
    # Write the class once, and use it many times. 
    # We'll see this a lot when we use dataframes to hold tables of data. 
    # Many popular libraries provide reusuable classes. 
    # It's a powerful way to organize code when dealing with many objects of the same type.

    for object in object_list:
        logger.info(object)
        logger.info(f"Count: {object.count()}")
        logger.info(f"Sum: {object.sum()}")
        logger.info(f"Mean: {object.mean()}")
        logger.info(f"Median: {object.median()}")
        logger.info("------------------")

    # Read log file and print it to the terminal
    with open(logname, 'r') as file_wrapper:
      print(file_wrapper.read())