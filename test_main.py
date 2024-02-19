import contextlib
import subprocess
import sys
import unittest

# limit number of retries
MAX_RETRIES = 5
retries = 0

# Force reload of autograding submodule
# This allows it to be updated even after students have accepted an assignment
# It would otherwise require them to delete and re-accept the assignment
# (or alternatively update the submodule manually)
def unload():
    global autograding
    if "autograding" in sys.modules:
        del sys.modules["autograding"]
    with contextlib.suppress(NameError):
        del autograding

unload()
subprocess.run(["git", "submodule", "update", "--init", "--remote"])
import autograding
from autograding.case import FuncCall, InOut


class TestSF(autograding.TestInputOutput):
    def setUp(self):
        self.testcases = [
            InOut(input="56", output="The duration is 0 hours, 0 minutes, and 56 seconds."),
            InOut(input="2846", output="The duration is 0 hours, 47 minutes, and 26 seconds."),
            InOut(input="3694", output="The duration is 1 hours, 1 minutes, and 34 seconds."),
        ]


if __name__ == '__main__':
    unittest.main()
