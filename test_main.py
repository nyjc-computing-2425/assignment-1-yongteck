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
    proc = subprocess.Popen(["python", "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True)
    try:
        stdout, stderr = proc.communicate(input=input_, timeout=1)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()
    finally:
        # Strip prompt from stdout; use colon to detect
        if stdout.strip():
            stdout = stdout[stdout.find(':') + 1:].lstrip()
        return stdout


class TestInputOutput(unittest.TestCase):

    def test_seconds_only(self):
        testcase = "56\n"
        testans = "The duration is 0 hours, 0 minutes, and 56 seconds.\n"
        userans = invoke_main(testcase)
        
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_minutes_and_seconds(self):
        testcase = "2846\n"
        testans = "The duration is 0 hours, 47 minutes, and 26 seconds.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")
        
    def test_part3(self):
        testcase = "3694\n"
        testans = "The duration is 1 hours, 1 minutes, and 34 seconds.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")
            

if __name__ == '__main__':
    unittest.main()
