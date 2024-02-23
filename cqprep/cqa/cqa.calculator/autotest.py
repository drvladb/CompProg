import subprocess
import sys
from pathlib import Path
import io
import zipfile

# TO USE - PLACE ZIP FILE (ANY NAME) IN CURRENT DIRECTORY

solutions = {}

tabulate = "regular" # "super" | "regular" | "none"

solnfile = open(list(Path(".").glob("*.zip"))[0], "rb")
with zipfile.ZipFile(io.BytesIO(solnfile.read())) as thezip:
    for zipinfo in thezip.infolist():
        with thezip.open(zipinfo) as ifile:
            solution_number = int(zipinfo.filename.split(".")[0])
            solution_type = zipinfo.filename.split(".")[1]
            if solution_number not in solutions.keys():
                solutions[solution_number] = {}
            solutions[solution_number][solution_type] = ifile.read().decode()
solnfile.close()

fail = False
for i, testcase in solutions.items():
    print(f"Case {i}: ", end="")
    # print(testcase)
    command = [sys.executable, 'solution.py']
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.communicate(input=testcase["in"].encode())[0]
    # print(output.decode())
    prog_out = output.decode()
    if prog_out == testcase["out"]:
        print("PASS")
    else:
        print("FAIL")
        fail = True
        if tabulate == "regular" or tabulate == "super":
            in_line = testcase["in"].split("\n")[1:]
            exp_out_line = testcase["out"].split("\n")
            got_out_line = prog_out.split("\n")

            for i in range(max(len(exp_out_line), len(got_out_line))):

                if len(in_line) > i and tabulate == "super":
                    print(in_line[i], end="")
                print("", end="\t")

                if len(exp_out_line) > i:
                    print(exp_out_line[i], end="")
                print("", end="\t")

                if len(got_out_line) > i:
                    print(got_out_line[i], end="")
                print()

        else:
            print("EXPECTED:")
            print(testcase["out"])
            print("GOT:")
            print(prog_out)

if fail:
    print("GO FIT IT!!!!")
else:
    print("SUBMIT!!!!!!")
