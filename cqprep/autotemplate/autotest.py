import subprocess
import sys
from pathlib import Path
import io
import zipfile

# TO USE - PLACE ZIP FILE (ANY NAME) IN CURRENT DIRECTORY

solutions = {}

solnfile = open(list(Path(".").glob("*.zip"))[0], "rb")
with zipfile.ZipFile(io.BytesIO(solnfile.read())) as thezip:
    for zipinfo in thezip.infolist():
        with thezip.open(zipinfo) as ifile:
            solution_number = int(zipinfo.filename.split(".")[0])
            solution_type = zipinfo.filename.split(".")[1]
            if solution_number not in solutions.keys():
                solutions[solution_number] = {}
            solutions[solution_number][solution_type] = ifile.read()
solnfile.close()

for i, testcase in solutions.items():
    print(f"Case {i}: ", end="")
    print(testcase)
    command = [sys.executable, 'solution.py']
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.communicate(input=testcase["in"].encode())[0]
    print(output.decode())
