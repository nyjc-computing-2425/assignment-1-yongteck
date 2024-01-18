import subprocess
import unittest


def strip_prompt(stdout: str) -> str:
    """Strip the prompt from stdout.
    The prompt is assumed to end with a colon (:), followed by zero or more
    whitespace characters.
    """
    if stdout.strip():
        stdout = stdout[stdout.find(':') + 1:].lstrip()
    return stdout


def invoke_main(input_: str) -> str:
    """Invoke main.py and return its output."""
    result: subprocess.CompletedProcess = subprocess.run(
        ["python", "main.py"],
        input=input_,
        capture_output=True,
        text=True,
        timeout=3,
    )
    stdout = result.stdout
    if not stdout or stdout.strip():
        return ""
    return strip_prompt(stdout) if ":" in stdout else stdout


class TestInputOutput(unittest.TestCase):

    def check_result(self, result: str, answer: str):
        """Test the user's answer against the expected answer."""
        if answer != "":
            self.assertNotEqual(result.strip(), "", msg=f"No output from program.")
        self.assertIn(result,
          answer,
          msg=f"User output {result!r} != expected output {answer!r}")

    def test_seconds_only(self):
        testcase = "56\n"
        testans = "The duration is 0 hours, 0 minutes, and 56 seconds.\n"
        userans = invoke_main(testcase)
        self.test_result(userans, testans)

    def test_minutes_and_seconds(self):
        testcase = "2846\n"
        testans = "The duration is 0 hours, 47 minutes, and 26 seconds.\n"
        userans = invoke_main(testcase)
        self.test_result(userans, testans)        

    def test_part3(self):
        testcase = "3694\n"
        testans = "The duration is 1 hours, 1 minutes, and 34 seconds.\n"
        userans = invoke_main(testcase)
        self.test_result(userans, testans)        
            

if __name__ == '__main__':
    unittest.main()
