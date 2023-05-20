"""
Creator: Tyler Stanton

44-608, Fundamentals of Data Analytics
Project 2 - Task 3

The purpose of this code is to calculate the different values of a local pool.

"""

# This imports the math package or certain calculations.
import math

# This sets up the logger to log the output of the file.
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Setting up variables as general integers.
width = int
length = int

# Defining a function to multiply width and length together.
def get_area_of_pool(width,length):
    return width * length

# Sets up specific outputs for the logger.
if __name__ == "__main__":

    # Calculating combinations and permutations under the math package.
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")

    # Calulating the area of pools from different widths and lengths.
    logger.info(f"get_area_of_pool(15,30) = {get_area_of_pool(15,30)}")
    logger.info(f"get_area_of_pool(60,100) = {get_area_of_pool(60,100)}")
    logger.info(f"get_area_of_pool(4,4) = {get_area_of_pool(4,4)}")


# Setting up variables as general integers.
num_adults = int
num_children = int

# Defining different functions for calculations using adult and children guests at a local pool.
def tot_num_of_guests(num_adults, num_children):
    return num_adults + num_children

def inc_gained_from_guests(num_adults, num_children):
    return math.fsum([num_adults * 8, num_children * 5])

def adult_to_children_ratio(num_adults, num_children):
    return round(num_adults / num_children, 2)

# Sets up specific outputs for the logger.
if __name__ == "__main__":

    # Sending output using the defined functions with specific values.
    logger.info(f"tot_num_of_guests(27,23) = {tot_num_of_guests(27,23)} total guests")
    logger.info(f"inc_gained_from_guests(27,23) = ${inc_gained_from_guests(27,23)} received today")
    logger.info(f"adult_to_children_ratio(27,23) = {adult_to_children_ratio(27,23)} adults to children")



