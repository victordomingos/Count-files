import unittest
from tests.test_argument_parser import TestArgumentParser
from tests.test_some_functions import TestSomeFunctions
from tests.test_viewing_modes import TestViewingModes


def suite():
    """Run all tests except performance tests.
    :return:
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestArgumentParser))
    test_suite.addTest(unittest.makeSuite(TestSomeFunctions))
    test_suite.addTest(unittest.makeSuite(TestViewingModes))
    return test_suite


# run all suite tests from root directory:
# python tests/test_runner.py

# or run file in PyCharm


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
