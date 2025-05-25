import sys
from checker import Checker

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 main.py <codeforces_problem_link> <solution_command> [args...]")
        print("Example: python3 main.py https://codeforces.com/problemset/problem/1/A python3 mysolution.py")
        return

    problem_link = sys.argv[1]
    solution_cmd = sys.argv[2:]  # e.g., ["python3", "mysolution.py"]
    checker = Checker(problem_link)

    print("Fetching problem statement and test cases...")
    checker.fetch_problem()
    if not checker.test_cases:
        print("Failed to fetch problem details or no test cases found.")
        return

    print("Running tests...")
    results = checker.run_tests(solution_cmd)
    checker.display_results(results)

if __name__ == "__main__":
    main()