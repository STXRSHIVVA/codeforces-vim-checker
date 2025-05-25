def parse_codeforces_url(url):
    # Validate and parse the Codeforces problem URL
    if "codeforces.com/problemset/problem/" not in url:
        raise ValueError("Invalid Codeforces problem URL")
    problem_id = url.split("/")[-1]
    return problem_id

def format_output(results):
    # Format the output results for display
    output = []
    for result in results:
        output.append(f"Test case {result['case']}: {'Passed' if result['passed'] else 'Failed'}")
    return "\n".join(output)

def read_input_file(file_path):
    # Read input from a specified file
    with open(file_path, 'r') as file:
        return file.read()

def write_output_file(file_path, content):
    # Write output to a specified file
    with open(file_path, 'w') as file:
        file.write(content)