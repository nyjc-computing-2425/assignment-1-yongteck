import unittest


from autograding import TestInputOutput, TestFunction
from autograding.case import InOut, FuncCall


class TestSF(TestInputOutput):
    def setUp(self):
        self.testcases = [
            InOut(input="56", output="The duration is 0 hours, 0 minutes, and 56 seconds."),
            InOut(input="2846", output="The duration is 0 hours, 47 minutes, and 26 seconds."),
            InOut(input="3694", output="The duration is 1 hours, 1 minutes, and 34 seconds."),
        ]


if __name__ == '__main__':
    import os
    if not os.listdir("autograding"):
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
    unittest.main()
