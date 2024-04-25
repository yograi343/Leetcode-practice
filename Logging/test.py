import logging

logger1 = logging.getLogger(__name__)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("employee1.log")
file_handler.setFormatter(formatter)
logger1.addHandler(file_handler)
logging.basicConfig(level=logging.DEBUG)


class test:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger1.debug("Created Employee: {} - {}".format(self.fullname, self.email))

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = test("John", "Smith")
emp_2 = test("Corey", "Schafer")
emp_3 = test("Yogesh", "Rai")
