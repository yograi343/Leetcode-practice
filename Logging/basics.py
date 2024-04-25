import logging
import test

""" 
DEBUG: detailed information, typically or interest only when diagnosing problems
INFO: configuration that things are working as expected
Warning: an Indication that something happened or indicates or some problem in the near future (e.g 'disk
space low').
Error: Due to more serious problem the sofware has not able to perform some functions.
Critical: A serios Error, indicating the program itself may be unable to continue running.
"""
logging.basicConfig(
    filename="sample.log",
    level=logging.DEBUG,
    format="%(name)s:%(levelname)s:%(message)s}",
)


def add(x, y):
    """Add function"""
    return x + y


def substract(x, y):
    """Subtract function"""
    return x - y


num_1 = 10
num_2 = 5
add_result = add(num_1, num_2)
logging.debug("Add: {}+{}={}".format(num_1, num_2, add_result))
subs_result = substract(num_1, num_2)
logging.debug("Subtract: {}-{}={}".format(num_1, num_2, subs_result))
