import requests
from bs4 import BeautifulSoup
import subprocess
import os

class Checker:
    def __init__(self, url):
        self.url = url
        self.problem_statement = None
        self.test_cases = []

    def fetch_problem(self):
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        def extract_text_with_newlines(pre):
            return pre.get_text(separator='\n').strip()
        inputs = [extract_text_with_newlines(pre) for pre in soup.select(".input pre")]
        outputs = [extract_text_with_newlines(pre) for pre in soup.select(".output pre")]
        self.test_cases = list(zip(inputs, outputs))

    def run_tests(self, user_solution):
        # If user_solution is a C++ source file, compile it first
        if isinstance(user_solution, list) and len(user_solution) == 1 and user_solution[0].endswith('.cpp'):
            cpp_file = user_solution[0]
            exe_file = os.path.splitext(cpp_file)[0]
            compile_cmd = ['g++', cpp_file, '-o', exe_file]
            result = subprocess.run(compile_cmd, capture_output=True)
            if result.returncode != 0:
                print("Compilation failed:")
                print(result.stderr.decode())
                return []
            user_solution = ['./' + exe_file]
        results = []
        for test_case in self.test_cases:
            result = self.run_single_test(user_solution, test_case)
            results.append(result)
        return results

    def run_single_test(self, user_solution, test_case):
        input_data, expected_output = test_case
        try:
            proc = subprocess.run(
                user_solution,
                input=input_data.encode(),
                capture_output=True,
                timeout=2
            )
            actual_output = proc.stdout.decode().strip()
            # Compare outputs line by line, ignoring leading/trailing whitespace
            expected_lines = [line.strip() for line in expected_output.strip().splitlines() if line.strip() != ""]
            actual_lines = [line.strip() for line in actual_output.strip().splitlines() if line.strip() != ""]
            passed = expected_lines == actual_lines
        except Exception as e:
            actual_output = str(e)
            passed = False
        return {
            "input": input_data,
            "expected": expected_output.strip(),
            "actual": actual_output,
            "passed": passed
        }

    def display_results(self, results):
        for idx, result in enumerate(results, 1):
            status = "Passed" if result["passed"] else "Failed"
            print(f"Test case {idx}: {status}")
            if not result["passed"]:
                print(f"  Input:\n{result['input']}")
                print(f"  Expected:\n{result['expected']}")
                print(f"  Actual:\n{result['actual']}")