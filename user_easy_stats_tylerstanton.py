"""
Creator: Tyler Stanton

44-608, Fundamentals of Data Analytics
Project 2 - Task 4

The purpose of this code is to calculate statistical values from two data sets and comparing them together.

"""

# importing packages into the file
import statistics
import turtle  
import sys  

# This sets up the logger to log the output of the file.
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Creating two lists of data, one showing temperatures in fahrenheit, and the other showing ice cream sales
temp_in_F = [54, 57, 59, 61, 63, 64, 65, 67, 72, 73, 74, 77]
ice_cream_sales = [19, 21, 33, 32, 41, 42, 41, 41.5, 52, 45, 55, 61]

# This quits the file if X and Y lists are not equal lengths
if len(temp_in_F) != len(ice_cream_sales):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(temp_in_F)}!={len(ice_cream_sales)}")
    quit()

# This warns user about Python version requirements
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# If the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# Finds correlation between lists
xx_corr = statistics.correlation(temp_in_F, temp_in_F)
xy_corr = statistics.correlation(temp_in_F, ice_cream_sales)

# Log the information 
logger.info("Here's some data with two lists:")
logger.info(f"temp_in_F:{temp_in_F}")
logger.info(f"ince_cream_sales:{ice_cream_sales}")
logger.info(f"correlation between temp_in_F and temp_in_F = {xx_corr:.2f}")
logger.info(f"correlation between temp_in_F and ice_cream_sales = {xy_corr:.2f}")

# Central tendancy of X list
meanX = statistics.mean(temp_in_F)
medianX = statistics.median(temp_in_F)
modeX = statistics.mode(temp_in_F)

# Central tendancy of Y list
meanY = statistics.mean(ice_cream_sales)
medianY = statistics.median(ice_cream_sales)
modeY = statistics.mode(ice_cream_sales)

# Output of X list's central tendancy
logger.info("Here are the central tendancy values of the X list:")
logger.info(f"mean of X value = {meanX:.2f}")  
logger.info(f"median of X value = {medianX:.2f}")
logger.info(f"mode of X value = {modeX:.2f}")

# Output of Y list's central tendancy
logger.info("Here are the central tendancy values of the Y list:")
logger.info(f"mean of Y value = {meanY:.2f}")  
logger.info(f"median of Y value = {medianY:.2f}")
logger.info(f"mode of Y value = {modeY:.2f}")

# Descriptive: Measures of spread

varX = statistics.variance(temp_in_F)
stdevX = statistics.stdev(temp_in_F)
lowestX = min(temp_in_F)
highestX = max(temp_in_F)

varY = statistics.variance(ice_cream_sales)
stdevY = statistics.stdev(ice_cream_sales)
lowestY = min(ice_cream_sales)
highestY = max(ice_cream_sales)

# Output of X list's measures of spread
logger.info("Here are the measures of spread values of the Y list:")
logger.info("var of X values = " + str(varX))
logger.info("stdev of X values = " + str(stdevX))
logger.info("lowest of X values= " + str(lowestX))
logger.info("highest of X values = " + str(highestX))

# Output of Y list's measures of spread
logger.info("Here are the measures of spread values of the Y list:")
logger.info("var of Y values = " + str(varY))
logger.info("stdev of Y values = " + str(stdevY))
logger.info("lowest of Y values= " + str(lowestY))
logger.info("highest of Y values = " + str(highestY))


# Creating a graph of the X and Y values and their correlation


slope, intercept = statistics.linear_regression(temp_in_F, ice_cream_sales)

# Choose an x value off in the future (future x)
future_x = 85

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"x:{temp_in_F}")
logger.info(f"y:{ice_cream_sales}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   At future x = {future_x:d},")
logger.info(f"   we predict the value of y will be { future_y:d}.")
logger.info("How'd we do? Does this make sense given the data?")
logger.info("Remember to close the app. Control c (or d or z maybe) to close it.")

# is the user ready to see a chart?
# TODO: change this to True when ready
ready_for_chart = False

logger.info(f"ready_for_chart = {ready_for_chart}")

# if ready for the chart, show the data, the best fit line, and the future prediction

if ready_for_chart:

    screen = turtle.Screen()
    screen.title("Linear Regression and Prediction")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(3)  # range 1-10  (slow-fast)

    w, h = screen.window_width(), screen.window_height()
    # e.g. 512, 480

    # Draw Axes
    t.penup()
    t.goto(w / 2, 0)
    t.pendown()
    t.goto(-w / 2, 0)
    t.penup()
    t.goto(0, h / 2)
    t.pendown()
    t.goto(0, -h / 2)

    # draw points
    for index, year in enumerate(temp_in_F):
        t.penup()
        t.goto(temp_in_F[index], ice_cream_sales[index])
        t.pendown()
        t.pencolor("blue")
        t.dot(20)

    # draw best-fit line
    h = int(slope * w + intercept)
    t.penup()
    t.goto(w, h)
    w = -w
    h = int(slope * w + intercept)
    t.pencolor("green")
    t.pensize(2)
    t.pendown()
    t.goto(w, h)

    # draw prediction dot
    t.penup()
    t.goto(future_x, future_y)
    t.pendown()
    t.pencolor("red")
    t.dot(20)

    turtle.done()
    screen.mainloop()
    logger.info("Done with the chart.")

else:
    logger.info("Ready for a chart? Edit this program to see an illustration.\n")

# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())


