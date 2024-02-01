import sys
import unittest

# autograding submodule might not be successfully pulled on init
# if unsuccessful, we have to pull it manually
# limit number of retries
MAX_RETRIES = 5
retries = 0
while "autograding" not in sys.modules:
    try:
        import autograding
        from autograding.case import FuncCall, InOut
    except ImportError:
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
        retries += 1
    if retries >= MAX_RETRIES:
        sys.exit("[import autograding] Too many retries, exiting")


class TestSF(autograding.TestInputOutput):
    def setUp(self):
        self.testcases = [
            InOut(input="56", output="The duration is 0 hours, 0 minutes, and 56 seconds."),
            InOut(input="2846", output="The duration is 0 hours, 47 minutes, and 26 seconds."),
            InOut(input="3694", output="The duration is 1 hours, 1 minutes, and 34 seconds."),
        ]


if __name__ == '__main__':
    unittest.main()
