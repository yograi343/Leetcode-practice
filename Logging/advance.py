import logging
import employee

logger = logging.getLogger(__name__)

formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("Logging/employee.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


num_1 = 10
num_2 = 5


def add(x, y):
    """Add the two numbers"""
    return x + y


def substract(x, y):
    """Subtract the two numbers return the difference"""
    return x - y


add_result = add(num_1, num_2)
logger.info("Add: {}+{}={}".format(num_1, num_2, add_result))

substract_result = substract(num_1, num_2)
logger.info("Subtract: {}-{}={}".format(num_1, num_2, substract_result))
